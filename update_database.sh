psql -c "DROP table studentcourse; DROP table student;drop table course; drop table department;drop table migratehistory"

rm -rf migrations
rm -rf migrations.json

pem init

#pem add app.models.[filename].[classname]
pem add flaskapp.models.Department
pem add flaskapp.models.Course
pem add flaskapp.models.Student
pem add flaskapp.models.StudentCourse

pem watch
pem migrate

rm -rf migrations
rm -rf migrations.json

< data.sql psql
