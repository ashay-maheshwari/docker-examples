from flask import Flask, render_template
import datetime

app = Flask(__name__)

#Default page to be loaded 
@app.route("/")
def index():
    return render_template('index.html')


#Load date route
@app.route("/date")
def date_today():
    return render_template('datetoday.html', utc_dt = datetime.datetime.utcnow())