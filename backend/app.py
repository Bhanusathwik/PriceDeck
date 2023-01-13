from flask import Flask
import re
from flask_cors import CORS
from operator import itemgetter

from scraper import scrape, scrape_link
from data import get_data_to_scrape, get_data_to_link_scrape

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    return {"Message": "Hello Welcome!"}


@app.route("/scrape/<product>")
def scraper_main(product="tv"):
    product = re.sub(" ", "+", product)
    flipkart_data_to_scrape = get_data_to_scrape("flipkart", product)
    amazon_data_to_scrape = get_data_to_scrape("amazon", product)

    data_list = []

    for data in scrape(flipkart_data_to_scrape):
        data_list.append(data)

    for data in scrape(amazon_data_to_scrape):
        data_list.append(data)

    data_list = [d for d in data_list if d['Price']
                 is not None and d['Link'] is not None]

    data_list = sorted(data_list, key=lambda i: i['Price'])

    return data_list


@app.route("/scrape_link/<uid>")
def scrape_data(uid):
    if not firebase_admin._apps:
        cred = credentials.Certificate("price-deck-10f0b298a802.json")
        app = firebase_admin.initialize_app(cred)
    firestore_client = firestore.client()

    coll_ref = firestore_client.collection(
        'users').document(uid).collection("products")

    # Using coll_ref.stream() is more efficient than coll_ref.get()
    docs = coll_ref.stream()

    for doc in docs:
        doc_dict = doc.to_dict()
        website = doc_dict['Product_website']
        link = doc_dict['Product_Link']

        data, header = get_data_to_link_scrape(website)
        price = scrape_link(data, header, link)

        ref = coll_ref.document(doc.id)

        ref.update({u'Latest_Price': price})

    return {"Message": "Success"}


if __name__ == '__main__':
    app.run(debug=True)
