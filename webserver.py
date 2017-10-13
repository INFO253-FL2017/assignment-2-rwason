"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return index() # Render the template located in "templates/index.html"

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('AboutUs.html')

@app.route('/contact')
def contact():
	return render_template('ContactUs.html')

@app.route('/blog/8-experiments-in-motivation')
def blog_experiments():
	return render_template('8ExperimentsinMotivation.html')

@app.route('/blog/a-mindful-shift-of-focus')
def blog_focus():
	return render_template('AMindfulShiftofFocus.html')

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog_direction():
	return render_template('HowtoDevelopanAwesomeSenseofDirection.html')

@app.route('/blog/training-to-be-a-good-writer')
def blog_writer():
	return render_template('TrainingtoBeaGoodWriter.html')

@app.route('/blog/what-productivity-systems-wont-solve')
def blog_productivity():
	return render_template('WhatProductivitySystemsWontSolve.html')