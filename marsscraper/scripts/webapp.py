
import argparse
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from marsscraper import scrape


argparser = argparse.ArgumentParser(
    description="Runs Flask scrapper application server",
    epilog="Example of use: `python -m marsscraper.scripts.webapp.py --host 127.0.0.1 --port 5000 --webdriver chrome --driverpath /usr/local/bin/chromedriver`"
)

argparser.add_argument(
    "-s",
    "--host",
    type=str,
    default="127.0.0.1",
    help="Host name to listen. Default=`127.0.0.1` (local host)"
)

argparser.add_argument(
    "-p",
    "--port",
    type=int,
    default=5001,
    help="Port to listen. Default=5000 "
)

argparser.add_argument(
    "-w",
    "--webdriver",
    type=str,
    default="chrome",
    help="Web driver name. Default=`chrome`"
)

argparser.add_argument(
    "-d",
    "--driverpath",
    type=str,
    default="/usr/local/bin/chromedriver",
    help="Web driver path. Default=`/usr/local/bin/chromedriver`"
)


app = Flask(__name__)

# create connection variable
conn = "mongodb://localhost:27017"

# pass connection to pymongo.MongoClient instance
client = MongoClient(conn)

# connect to mars database. (one will be created if not already available)
db = client.mars

collections = db.scrapes


@app.route("/")
def home_view():
    mars_dict = collections.find_one()
    return render_template("index.html", dict=mars_dict)


@app.route("/hemisphere/<x>")
def hemisphere_view(x):
    mars_dict = collections.find_one()
    return render_template("hemisphere.html",
                           dict=mars_dict,
                           hemisphere_dict=mars_dict["hemisphere_image_urls"][int(x)])


@app.route("/scrape")
def scrape_new_data():
    mars_dict = scrape(driver=args.webdriver, driverpath=args.driverpath)
    collections.update({"id": 1}, {"$set": mars_dict}, upsert=True)
    return home_view()


if __name__ == "__main__":

    global args
    args = argparser.parse_args()
    app.run(debug=True, host=args.host, port=args.port)