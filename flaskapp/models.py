"""
Models to represent database objects
"""
from peewee import *
from datetime import datetime

mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb

""" ----------------------------------------------
    Final Models
---------------------------------------------- """
class Department(baseModel):
    department_id = IntegerField(primary_key=True)
    name = CharField(30)
    division = IntegerField(null=True)

class Committee(baseModel):
    committee_id = IntegerField(primary_key=True)
    name = CharField(255)
    abbreviation = CharField(32,null=True)

    def to_dict(self):
        return {
            'name': self.name,
            'abbreviation': self.abbreviation
        }

class Person(baseModel):
    person_id = IntegerField(primary_key=True)
    first_name = CharField(30)
    last_name = CharField(30)
    tenure_status = CharField(30)
    employee_class = CharField(30)
    position_title = CharField(255)
    is_exempt = BooleanField(default=True)
    primary_dept = ForeignKeyField(Department)
    secondary_dept = ForeignKeyField(Department)

    class Meta:
        indexes = ((("first_name", "last_name"), True))

class AssignedCommittee(baseModel):
    assigned_committee_id = IntegerField(primary_key=True)
    person = ForeignKeyField(Person)
    committee = ForeignKeyField(Committee) 
    academic_year = FixedCharField(9)
    is_current = BooleanField(default=False)

    class Meta:
        table_name = 'assigned_committee'

class Survey(baseModel):
    survey_id = IntegerField(primary_key=True)
    person = ForeignKeyField(Person)
    academic_year = FixedCharField(9)
    current_adhoc = CharField(null=True)
    expected_adhoc = CharField(null=True)
    time_off_campus = CharField(null=True)
    comments = TextField(null=True)
    taken_on = DateTimeField(default=datetime.now)

class SurveyPreference(baseModel):
    survey = ForeignKeyField(Survey)
    committee = ForeignKeyField(Committee)
    rank = IntegerField()

    class Meta:
        table_name = 'survey_preference'
        primary_key = False

""" ----------------------------------------------
    Raw Models
---------------------------------------------- """
class AlphaList(baseModel):
    class Meta:
        table_name = 'alpha_list'
        schema = 'raw'
        primary_key = False

    lastname = CharField()
    firstname = CharField()
    committee = CharField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.committee}"
    
class CommitteeMap(baseModel):
    class Meta:
        table_name = 'committee_map'
        schema = 'raw'
        primary_key = False

    fullname = CharField(255)
    abbr = CharField(255)

    def __str__(self):
        return f"{self.fullname} - {self.abbr}"

class EmployeeClass(baseModel):
    class Meta:
        table_name = 'employee_class'
        schema = 'raw'
        primary_key = False

    employee_class = CharField(255)
    status = CharField(255)
    position_title = CharField(255)
    last_name = CharField(255)
    first_name = CharField(255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FacultyList(baseModel):
    class Meta:
        table_name = 'faculty_list'
        schema = 'raw'
        primary_key = False

    last_name = CharField(255)
    first_name = CharField(255)
    primary_dept = CharField(255)
    secondary_dept = CharField(255)
    div = IntegerField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class HistoricalCommittees(baseModel):
    class Meta:
        table_name = 'historical_committees'
        schema = 'raw'
        primary_key = False

    tenure_status = CharField(255)
    y2017 = CharField(255,column_name='2017-2018')
    y2018 = CharField(255,column_name='2018-2019')
    y2019 = CharField(255,column_name='2019-2020')
    y2020 = CharField(255,column_name='2020-2021')
    y2021 = CharField(255,column_name='2021-2022')
    y2022 = CharField(255,column_name='2022-2023')
    last_name = CharField(255)
    first_name = CharField(255)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class PreferenceSurvey(baseModel):
    class Meta:
        table_name = 'preference_survey'
        schema = 'raw'
        primary_key = False

    last_name = CharField(255)
    first_name = CharField(255)
    first = CharField(255)
    second = CharField(255)
    third = CharField(255)
    fourth = CharField(255)
    adhoc_22_23 = CharField(255)
    adhoc_23_24 = CharField(255)
    time_off = CharField(255)
    comments = CharField(255)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"