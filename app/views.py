from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
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
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''

    return render_template ('news.html', id = news_id )
