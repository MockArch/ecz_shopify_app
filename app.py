import os
from flask import Flask, request, redirect, url_for, Response
from pprint import pprint


app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
URL = "https://shopifyec.herokuapp.com/"
ACCESS_SCOPE = 'read_orders, write_products'

@app.route('/')
def homepage():

    return """
    <h1>Hello Shopify app</h1>"""


@app.route('/shopify')
def shopify_install():
    # hmac = request.args.get("hmac")
    if request.args.get("shop"):
        shop = request.args.get("shop")
    else:
        return Response(response="Error: parameter shop not found ", status=500)
    r_url = URL + '/shopify/callback'    
    auth_url = 'https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}'.format(
        shop, API_KEY , ACCESS_SCOPE , r_url)
    # r = "the hmac return value is " + hmac + "and " + " the shop name is " + shop
    print("Debug - auth URL: ", auth_url)
    return redirect(auth_url)


@app.route('/shopify/callback')
def shopify_callback():
    return "REDIRECT URL"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
