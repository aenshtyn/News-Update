from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # #Getting popular news
    # popular_news = get_news('popular')
    # print(popular_news)
    title = 'Home - Your best news Source'
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''

    return render_template ('news.html', id = news_id )

# def index():
#
#     '''
#     View root page function that returns the index page and its data
#     '''
#
#     title = 'Home - Your Best News Source'
#     return render_template('index.html', title = title)
