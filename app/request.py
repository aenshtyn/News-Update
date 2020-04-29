import urllib.request,json
from .models import Source,Article

# Getting Api Key
api_key = None
#Getting the base urls
source_base_url = None
article_base_url = None

def configure_request(app):
    global api_key,source_base_url,article_base_url
    api_key = app.config['SOURCE_API_KEY']
    source_base_url = app.config['SOURCE_BASE_URL']
    article_base_url = app.config['ARTICLE_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results

def get_articles(id):
    get_article_url = article_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        source_object = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

        return article_results
