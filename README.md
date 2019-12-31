<img src="https://github.com/billhong6981/Many-to-Many/blob/master/BH-logo.png" width="60" height="60" />

# Many-to-Many: Employee Data And Task Management Tool

## Project Name:
Many to Many Web App

## Deployment
The app is not responsive design currently, may re-design later.  
The app was deployed to Google Cloud [checkout on me](http://34.94.254.88)
[GitHub Landing Page](http://35.243.203.94/)  

## Description
This App is a searching and manipulation employee data and task management tool, specifically to handle management of complex interdependent tasks.  
You are welcome to checkout my blog post [Blog](https://www.linkedin.com/pulse/hand-on-project-your-friend-bill-huang/)

Many-to-Many application and website, including the database, storage, RESTful API, Web Framework, and Front End.  Currently the application is designed to run with Database Storage Engine:
To set up the databases, use command:  
```
cat /dev/8-dump.sql | mysql -uroot -p;
```
To connect to the MySQL database sever, user environment variable:
```
$ HBNB_MYSQL_USER=bh_dev HBNB_MYSQL_PWD=bh_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=bh_dev_db HBNB_TYPE_STORAGE=db \
[COMMAND HERE]
```

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __web server:__ nginx/1.4.6
* __application server:__ Flask 0.12.2, Jinja2 2.9.6
* __web server gateway:__ gunicorn (version 19.7.1)
* __database:__ mysql Ver 14.14 Distrib 5.7.18
* __documentation:__ flasgger==0.6.6
* __style sheet:__ CSS3
* __python:__ PEP 8 (v. 1.7.0)
* __web static:__ [W3C Validator](https://validator.w3.org/)
* __bash:__ ShellCheck 0.3.3


## Team Members
HongTu Huang (solo)


## Technologies
Using Python language to write the script on server side. Python is Object Oriented Programming(OOP), I use it to create Class Module match to each MySQL database table name. And python library SQLALchemy is used to ORM, mapping python Object to MySQL Relational Table, then we can Create, Update, Delete database via python script on the backend of server side.
MySQL is run on back-end as database server.
FLASK is used role as API on server.
In the Frontend, no use any Frameworks to help, pure HTML, CSS, JAVASCRIPT are used to compose and render webpages, either static or dynamic pages.


## Infrastructure
<img src="https://github.com/billhong6981/Many-to-Many/blob/master/dev/WebStack.png" />


## Databases
<img src="https://github.com/billhong6981/Many-to-Many/blob/master/dev/DataStructure.png" />


## Related Project
The good news is: Holberton School has current project AirBnB_Clone, it is a big project for the students in Holberton School, it took 4 months to do parts by parts. Many-to-Many App structure learn from AirBnB_Clone project. And will add user login validation feature and browser terminal to manipulate backend database feature to the App.


## Author
Bill Huang

## License
MIT License
