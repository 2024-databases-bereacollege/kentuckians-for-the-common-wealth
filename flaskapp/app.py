"""
This is the main views for our Course Registration Flask app
In terminal, switch to this directory, then start the server 
$ cd flaskapp/
$ flask run
When you see the popup "your application running on Port XXXX, click to open the webpage for the app!
You can also copy and paste the URL http://127.0.0.1:XXXX shown in the terminal into your browser
"""
from flask import Flask, render_template, g, request
from models import Course, StudentCourse
from logic import *
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def courseList():
    courses = Course.select()
    return render_template("courselist.html", 
                            page_title="Course List",
                            page_description="Choose from one of the available courses", 
                            courses=courses)

@app.route('/register', methods=['POST'])
def register():
    """
    """
    course_id = request.form.get('course_id')
    user_id = request.form.get('user_id')

    StudentCourse.insert(course=course_id,
                         student=user_id,registered_on=datetime.now()).execute()

    return ''

@app.route('/current/<int:id>', methods=['GET', 'POST'])
def currentCourses(id):
   ''' View courses for the given user
   '''
   return ""

@app.before_request
def load_user():
    g.user = Student.get_by_id(2)