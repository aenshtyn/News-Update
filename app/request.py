import urllib.request,json
from .models import news,source

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

    
def get_news(category):
    '''
    Function that gets the json response to out url request
    '''

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function that processes the news result and transforms into a list of objects


    Args:
        news_list: A list of dictionaries that contain news details

    Returns:
        news_result: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('urlToImage')


        if description:
            news_object = News(name,author,title,description,url,image)
            news_results.append(news_object)

    return news_results

def get_article(title):
    get_news_details_url = base_url.format(title,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = []
        if news_details_response:
            name = news_details_response.get('name')
            author = news_details_response.get('author')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            content = news_details_response.get('content')


            news_object = News(name,author,title,description,url,content)


    return news_object
