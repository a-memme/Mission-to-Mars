# Import dependencies 
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Setup flask 
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Setup Flask routes 

# Home page (i.e ("/"))
# PyMongo to find the "mars" collection in our database 
# return an HTML template using an index.html file 

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# access the database, scrape new data using scraping.py script, 
# and return a message when successful
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run(debug=True)