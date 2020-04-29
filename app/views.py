from flask import render_template
from app import app
from .request import get_sources,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting news sources
    general = get_sources('general')
    business = get_sources('business')
    science = get_sources('science')
    entertainment = get_sources('entertainment')
    health = get_sources('health')
    sports = get_sources('sports')
    technology = get_sources('technology')

    title = 'Home - Your best news Source'
    return render_template('index.html', title = title,science = science, entertainment = entertainment, health = health, sports = sports, technology = technology)

@app.route('/source/<source_id>')
def source(id):

    '''
    View source page function that returns the source details page and its data
    '''
    article = get_article(id)
    title = f'{source.id}'
    return render_template('source.html',title = title, article = article)
