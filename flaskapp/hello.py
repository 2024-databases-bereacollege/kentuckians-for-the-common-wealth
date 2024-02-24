"""
This is the starter API for the Flask app. 
In terminal, switch to this directory, then start the server 
$ cd flaskapp/
$ flask --app hello run
When you see the popup "your application running on Port XXXX, click to open the webpage for the app!
You can also copy and paste the URL http://127.0.0.1:XXXX shown in the terminal into your browser

"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello there, World!</p>"