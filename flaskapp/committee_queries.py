''' This file contains queries to the database to retrieve Committee specific information
'''
from models import *

def all_faculty_staff():
    eligible_people = Person.select().order_by(Person.last_name)
    roles = ["chair", "college faculty 1", "college faculty 2"]
    return roles, eligible_people

def ballot_for_COGE(id, selected_role):
    ''' Lists out people currently serving on Commmittee 11
    '''
    # selectedRole = selected_role
    roles = ["Appointed GSTR 110 Course Coordinator", "Appointed GSTR 210 Course Coordinator", "Appointed GSTR 310 Course Coordinator", "Appointed GSTR 410 Course Coordinator", "Appointed GSTR 332 Course Coordinator", "ALE Course Coordinator", "Appointed WELL Course Coordinator", "Associate Provost (ex officio)", "Student representative"]
    selection = [] 
    # valid_faculty = []  
    match selected_role:
            case 'Appointed GSTR 110 Course Coordinator':
                print("GSTR110 selected")
                selection = Person.select(Person.last_name, Person.first_name,Person.employee_class,Person.position_title,Person.person_id).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id))
                
                # selection = (Person.select(Person.last_name)) 
                # valid_faculty = [(last_name, first_name) for last_name, first_name in selection]

            case 'Appointed GSTR 210 Course Coordinator':
                selection = Person.select(Person.last_name, Person.first_name).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id)).where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty'))
                  # Conditional for persons in this seat for GenEd committee.

            case 'Appointed GSTR 310 Course Coordinator':
                selection = Person.select(Person.last_name, Person.first_name).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id)).where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty'))
                 # Conditional for persons in this seat for GenEd committee.

            case 'Appointed GSTR 410 Course Coordinator':
                selection = Person.select(Person.last_name, Person.first_name).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id)).where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty'))

                 # Conditional for persons in this seat for GenEd committee.

            case 'Appointed GSTR 332 Course Coordinator':
                selection = Person.select(Person.last_name, Person.first_name).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id)).where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty'))

                 # Conditional for persons in this seat for GenEd committee.

            case 'ALE Course Coordinator':
                selection = Person.select(Person.last_name, Person.first_name).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id)).where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty'))

                 # Conditional for persons in this seat for GenEd committee.

            case 'Appointed WELL Course Coordinator':
                selection = (Person.select(Person.last_name, Person.first_name).join(AssignedCommittee, JOIN.LEFT_OUTER, on = (Person.person_id == AssignedCommittee.person_id)).where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty')))

                 # Conditional for persons in this seat for GenEd committee.
        
            case _:
                #If unknown role selected, return a list of all faculty and staff
                def_roles, eligible_people = all_faculty_staff()
                selection = eligible_people

    return roles, selection

def ballot_for_CSRI( id, selected_role):
    print("in CSRI")
    query_faculty = (Person
         .select()
         .join(AssignedCommittee, JOIN.LEFT_OUTER, on=(Person.person_id==AssignedCommittee.person_id))
         .where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Faculty'))
         )
    query_staff = (Person
         .select()
         .join(AssignedCommittee, JOIN.LEFT_OUTER, on=(Person.person_id==AssignedCommittee.person_id))
         .where((AssignedCommittee.person_id.is_null(True)) & (Person.employee_class == 'Staff'))
         )
    
    slots = {'Chair': query_staff, 'College Faculty 1': query_faculty , 
                      'College Faculty 2': query_faculty, 'General Assembly 1':query_staff,
                      'Graduate 1': query_staff, 'Graduate 2': query_staff}

    if selected_role == 'faculty':
        selected_role = "College Faculty 1"
    return [key for key in slots],[person for person in slots[selected_role]]