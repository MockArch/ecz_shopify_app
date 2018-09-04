import os


class Config(object):
    SECRET_KEY = "CantStopAddictedToTheShinDigChopTopHeSaysImGonnaWinBig"
    HOST = "shopifyec.herokuapp.com"

    SHOPIFY_CONFIG = {
        'API_KEY': os.getenv('API_KEY'),
        'API_SECRET': os.getenv('SECRET_KEY'),
        'APP_HOME': 'http://' + HOST,
        'CALLBACK_URL': 'http://' + HOST + '/install',
        'REDIRECT_URI': 'http://' + HOST + '/connect',
        'SCOPE': 'read_products, read_collection_listings'
    }
