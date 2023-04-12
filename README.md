# Price Deck
A Price Comparison website
## Local Installation
1.  Open the terminal in the folder where you want to save the code file. 
2.  Clone the repository using the command `git clone https://github.com/cmdsiraj/PriceDeck.git`.
3.  Go to folder PriceDeck. You can use this command to navigate to that directory `cd .\PriceDeck\`.
4.  Installing dependencies: `npm install`.
5.  You can find the server files here: https://github.com/cmdsiraj/price-deck-server (clone this repo and place inside this folder (PriceDeck)
6.  cd to flask-server with the help of command  `cd .\flask-server\`.
7.  Creating virtual environment with the help of command `virtualenv venv`.
8.  Activate virtual environment using command `venv/Scripts/activate`.
9.  Download required libraries using the following command `pip install -r requirements.txt`
10.  Now, all the setup is ready. 
11. Open a terminal in PriceDeck Folder and execute `npm start` to start the react server. 
12. Open another terminal in the flask-server folder and execute `python server.py` to start our python server. 
13. Open a browser and go to `http://localhost:3000/`.
14. The app is up and ready to use. 

## Description about folders

1. `flask-server` is our main folder. This is the server where scrapping processing takes place. 
2. `src` folder contain all the files of the user interface of the application.

## files in flask-server

Inside the flask server, we have the following files `server.py`, 'scraper.py`, 'data.py`, 'alert.py` and `requirements.txt`.

1) `server.py` is the main server. This recives the requests from our react application. 
2) `scraper.py` contains our scrapping functions. 
3) `data.py` contains data which is used by `scraper.py`. This data is about the classes, tags and attributes and links that we need to scrape `flipkart` and `amazon` websites. 
4) `alert.py` this contains code which regularly checks for a price drop of products which are chosen by users and send emails about price drop to the products to respective products. 
5) `requirements.txt` contains details about libraries that are required by `.py` files. 
