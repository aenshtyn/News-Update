from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news, get_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    science = get_news('science')
    entertainment = get_news('entertainment')
    health = get_news('health')
    sports = get_news('sports')
    technology = get_news('technology')

    print(science)
    title = 'Home - Your best news Source'
    return render_template('index.html', title = title,science = science, entertainment = entertainment, health = health, sports = sports, technology = technology)
@main.route('/news/<int:title>')
def news(title):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_article(title)
    title = f'{news.title}'

    return render_template ('news.html', title = title, news = news )
