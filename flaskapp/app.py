"""
This is the main views for our Committee-Date Flask app
In terminal, switch to this directory, then start the server 
$ cd flaskapp/
$ flask run
When you see the popup "your application running on Port XXXX, click to open the webpage for the app!
You can also copy and paste the URL http://127.0.0.1:XXXX shown in the terminal into your browser

"""
from flask import Flask, render_template
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
    return render_template("courselist.html", page_title="Course List",
        page_description=description, 
        data=[com for com in Committee])

@app.route('/current/<int:id>', methods=['GET', 'POST'])
def currentCourses(id):
   ''' View courses for the given user
   '''
   comm_name  = Committee.get(id).name
   return f"<h1>{comm_name}</h1>"