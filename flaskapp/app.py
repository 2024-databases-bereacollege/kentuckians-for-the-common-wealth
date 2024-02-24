"""
This is the main views for our Committee-Date Flask app
In terminal, switch to this directory, then start the server 
$ cd flaskapp/
$ flask run
When you see the popup "your application running on Port XXXX, click to open the webpage for the app!
You can also copy and paste the URL http://127.0.0.1:XXXX shown in the terminal into your browser

"""
from flask import Flask, render_template
from models import Committee
from committee_queries import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    #return "<p>Hello there, World!</p>"

@app.route('/committeeList')
def committeeList():
    ''' list of columns names, all data
    '''
    descript = "Browse Berea College Governing Committees and Councils"
    
    return render_template("committees.html", page_title="Committee List",
        page_descript=descript, 
        data=[com for com in Committee])

@app.route('/committeePage/<int:id>', methods=['GET', 'POST'])
def committeePage(id):
   ''' todo: list out people currently serving on Commmittee #
   '''
   comm_name  = Committee.get(id).name
   return f"<h1>{comm_name}</h1>"

@app.route('/committeeList/<int:id>/ballot')
@app.route('/committeeList/<int:id>/ballot/<string:role>')
def committeeBallot(id, role='faculty'):
    ''' Based on Committee ID, call appropriate ballot generator function 
        default: 
    '''
    comm_name = Committee.get(id).name

    #todo: this switch statement will call each student team's ballot view function
    match comm_name.strip():
        case "Committee on General Education":
            roles, eligible_people = ballot_for_COGE( id, role)
        case "Athletic Affairs Committee":
            roles, eligible_people = ballot_for_Athletics( id, role)
        case "Sustainability Committee":
            roles, eligible_people = ballot_for_Sustainability( id, role)
        case "Convocation Committee":
            roles, eligible_people = ballot_for_Convocations( id, role)
        case "Committee for Socially Responsible Investing":
            roles, eligible_people = ballot_for_CSRI( id, role)
        case _:
            roles, eligible_people = all_faculty_staff()
            print(f"Committee {comm_name} not found in switch statement")

    if len(eligible_people) == 0:
        stdroles, eligible_people = all_faculty_staff()
    else:
        print(f"For {comm_name} display: {roles}")

    return render_template("ballot.html", page_title=f"Ballot for {comm_name}", eligible_people=eligible_people, selected_roles=roles)


@app.route('/api/cdata')
def cdata():
    return {'data': [c.to_dict() for c in Committee]}

