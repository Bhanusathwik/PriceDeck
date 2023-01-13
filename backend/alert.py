import schedule
import time
import smtplib
import firebase_admin
import re
from firebase_admin import credentials
from firebase_admin import firestore
from scraper import scrape_link
from data import get_data_to_link_scrape


def check():
    print("called")
    if not firebase_admin._apps:
        cred = credentials.Certificate("price-deck-10f0b298a802.json")
        app = firebase_admin.initialize_app(cred)
    firestore_client = firestore.client()

    users_ref = firestore_client.collection('users')
    users_docs = users_ref.stream()

    for user in users_docs:
        products_ref = firestore_client.collection(
            'users').document(user.id).collection("products")
        products_docs = products_ref.stream()

        for product in products_docs:
            website = product.to_dict()['Product_website']
            link = product.to_dict()['Product_Link']

            data, header = get_data_to_link_scrape(website)
            cur_price = scrape_link(data, header, link)

            # cur_price = 5

            price = product.to_dict()['Product_price']

            price = re.sub('[^0-9]', '', price)

            if cur_price < int(price):
                print(user.to_dict()['email'])
                notification(user.to_dict()['email'], product.to_dict()['Product_Name'], product.to_dict()[
                             'Product_Link'], product.to_dict()['Product_website'])
    print("checked")


def notification(receiver, product_name, link, website):
    
    
    sender_mail = 'database.siraj@gmail.com'    
    receivers_mail = [receiver]
    
    subject = "Price Fell Down"   
    body = "There is a price drop for {name}.\n\nPlease check {website}, click here {url}".format(
    name=product_name, website=website, url=link)
    msg = f"Subject:{subject}, \n\n{body}"    
    try:    
        smtpObj = smtplib.SMTP('gmail.com',587)   
        smtpObj.sendmail(sender_mail, receivers_mail, msg)    
        print("Successfully sent email")    
    except Exception:    
        print("Error: unable to send email") 
   
   


schedule.every().day.at("00:00").do(check)
print("started")
while True:
    schedule.run_pending()
    time.sleep(1)  # wait one minute












    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.ehlo()
    # server.starttls()
    # server.ehlo()
    # server.login('database.siraj@gmail.com', 'database@2022')

    # subject = "Price Fell Down"
    # body = "There is a price drop for {name}.\n\nPlease check {website}, click here {url}".formay(
    #     name=product_name, website=website, url=link)
    # msg = f"Subject:{subject}, \n\n{body}"

    # server.sendmail('database.siraj@gmail.com', receiver, msg)
    # print('mail sent')