from peewee import *

# Database Configuration
################################
mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb

""" ----------------------------------------------
    Final Models
---------------------------------------------- """
class Department(baseModel):
    name = CharField()
    abbr = CharField()
    division = IntegerField(null=True)

class Course(baseModel):
    name = CharField()
    number = IntegerField()
    instructor = CharField()
    department = ForeignKeyField(Department)

class Student(baseModel):
    name = CharField()
    bnumber = CharField()
    classlevel = CharField()

class StudentCourse(baseModel):
    student = ForeignKeyField(Student)
    course = ForeignKeyField(Course)
    registered_on = DateTimeField()
