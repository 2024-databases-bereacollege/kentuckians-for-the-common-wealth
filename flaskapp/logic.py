''' This file contains queries to the database to retrieve Committee specific information
'''
from models import *

def all_faculty_staff():
    eligible_people = Person.select().order_by(Person.last_name)
    roles = ["chair", "college faculty 1", "college faculty 2"]
    return roles, eligible_people
