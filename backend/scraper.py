import bs4
from bs4 import BeautifulSoup
import requests
#import re


def scrape(data):

    domain = data['domain']
    link = data['link']
    classes = data['classes']
    tags = data['tags']
    headers = data['headers']

    page = requests.get(link, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        main = soup.find(tags['main'], class_=classes['main'])
    except:
        return {"message": "Can't get the Page"}

    products = soup.find_all(
        tags['product_class'], class_=classes['product_class'][0])

    if len(products) == 0:
        if domain == 'https://www.flipkart.com':
            products = soup.find_all(
                tags['product_class'], class_=classes['product_class'][1])

    product_name = None
    product_price = None
    product_link = None
    product_image = None

    # my_data = []
    for i in range(3, len(products)):
        if type(products[i]) is bs4.element.Tag:
            try:
                product_name = products[i].find(
                    tags['name'][0], class_=classes['name'][0]).get_text()
            except:
                try:
                    if domain == 'https://www.amazon.in/':
                        product_name = products[i].find(
                            tags['name'][0], class_=classes['name'][1]).get_text()
                    else:
                        product_name = products[i].find(
                            tags['name'][1], class_=classes['name'][1])['title']

                except:
                    try:
                        product_name = products[i].find(
                            tags['name'][2], class_=classes['name'][2])['title']
                    except:
                        product_name = None

            try:
                product_price = products[i].find(
                    tags['price'], class_=classes['price']).get_text()
            except:
                product_price = None

            try:
                product_link = domain + \
                    products[i].find(tags['link'], class_=classes['link'][0])[
                        'href']
            except:
                try:
                    product_link = domain + \
                        products[i].find(tags['link'], class_=classes['link'][1])[
                            'href']
                except:
                    try:
                        product_link = domain + \
                            products[i].find(tags['link'], class_=classes['link'][2])[
                                'href']
                    except:
                        product_link = None
            try:
                product_image = products[i].find(
                    tags['image'], class_=classes['image'][0])['src']
            except:
                try:
                    product_image = products[i].find(
                        tags['image'], class_=classes['image'][1])['src']
                except:
                    product_image = None
            try:
                product_rating = products[i].find(
                    tags['rating'], class_=classes['rating']).get_text()[:3]
            except:
                product_rating = None

            data = {
                'Name': product_name,
                'Price': product_price,
                'Link': product_link,
                'Image': product_image,
                'Rating': product_rating,
                'Website': domain.split('.')[1].upper()
            }

            yield data

#   return


def scrape_link(data, header, link):
    page = requests.get(link, headers=header)

    price = None

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        price = soup.find(data['tag'], class_=data['class']).get_text()
    except:
        price = None
        print("Can't get the Price")

    return price
