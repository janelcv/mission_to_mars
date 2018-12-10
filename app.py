from flask import Flask, render_template, redirect
import scrape_mars
import pymongo
import json

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

app = Flask(__name__)

# @app.route("/")
# def home():
#    return "test"
#
# if __name__ == "__main__":
#     app.run(debug = True)

@app.route("/scrape")
def scrape_data():
    scraped_data = scrape_mars.scrape()
    mars_db = client.mars
    data = mars_db.mars_data
    data.delete_many({})
    data.insert(scraped_data)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug = True)


@app.route("/")
def index():
    mars_db = client.mars
    data = mars_db.mars_data.find_one()
    print(data)
    return render_template("index.html", data = data)


if __name__ == "__main__":
    app.run(debug=True)
