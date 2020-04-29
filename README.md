# Project Name
## News Updates app (https://moha-news-update2.herokuapp.com)


#### Built by

Mohamed Abdullahi  

## Description

This is a webapp that should be showing different news webites and once clicked they should redirect the user to read it from the source website. This app is built using the NEWS API - (https://newsapi.org/).

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

## Setup/Installation Requirements

* python3.7
* pip
* virtualenv


## Cloning
* In your terminal:

  $ git clone https://github.com/aenshtyn/News-Update/

  $ cd News-Updates

## Running the Application
* Creating the virtual environment

        $ python3.7 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.7 -m pip install Flask
        $ python3.7 -m pip install Flask-Bootstrap
        $ python3.7 -m pip install Flask-Script

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                python3.7 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.7 manage.py tests


## Known Bugs

The images arent showing as needed.

## Technologies Used

Python 3.7
Flask

## Support and contact details

If you have any issues or questions you can contact me at demahom93@gmail.com

###### LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
