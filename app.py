import os
from flask import Flask, request
from pprint import pprint


app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")


@app.route('/')
def homepage():

    return """
    <h1>Hello Shopify app</h1>"""


@app.route('/shopify')
def shopify_page():
    hmac = request.args.get("hmac")
    shop = request.args.get("shop")
    r = "the hmac return value is " + hmac + "and " + " the shop name is " + shop
    return r


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
