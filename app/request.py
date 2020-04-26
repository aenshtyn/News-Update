from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the News base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to out url request
    '''

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_date = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            new_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function that processes the news result and transfomr into a list of objects


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
        content = news_item.get('content')

    return news_results
