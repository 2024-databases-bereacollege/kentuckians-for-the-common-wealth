"""
This is the main views for our Course Registration Flask app
In terminal, switch to this directory, then start the server 
$ cd flaskapp/
$ flask run
When you see the popup "your application running on Port XXXX, click to open the webpage for the app!
You can also copy and paste the URL http://127.0.0.1:XXXX shown in the terminal into your browser
"""
from flask import Flask, render_template, g
from models import Course
from logic import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return render_template("index.html")
    return "<h1>Hello, World!</h1>"

@app.route('/courseList')
def courseList():
    courses = Course.select()
    return render_template("courselist.html", 
                            page_title="Course List",
                            page_description="Choose from one of the available courses", 
                            courses=courses)

@app.route('/current/<int:id>', methods=['GET', 'POST'])
def currentCourses(id):
   ''' View courses for the given user
   '''
   return ""

@app.before_request
def load_user():
    g.user = Student.get_by_id(2)