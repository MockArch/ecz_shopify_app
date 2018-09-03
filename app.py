import os
from flask import Flask, request
from pprint import pprint


app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
SECRET_KEY =  os.getenv("SECRET_KEY")

@app.route('/')
def homepage():

    return """
    <h1>Hello Shopify app</h1>"""


@app.route('/shopify')
def shopify_page():
    pprint(request)
    return "something is requested"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

