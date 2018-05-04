from flask import Flask, render_template
from flask_pymongo import MongoClient

scrape = Flask(__name__)


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


@app.route("/scrape")
def index():
	mars = db.mars.find_one()
	return render_template('index.html', mars=mars)

if __name__ == "__main__":
    app.run()