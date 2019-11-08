![][BH-logo.png]# Many-to-Many: a app for management todos

## 1. Project name:
Many to Many Web App

## Description
This App is a searching and manipulation employee data and task management tool, specifically to handle management of complex interdependent tasks.
The app was deployed at [visit website](http://35.243.203.94/)
You are welcome to checkout my blog post [Blog](https://www.linkedin.com/pulse/hand-on-project-your-friend-bill-huang/)


## Team Members
HongTu Huang (solo)

## 3. Technologies
Using Python language to write the script on server side. Python is Object Oriented Programming(OOP), I use it to create Class Module match to each MySQL database table name. And python library SQLALchemy is used to ORM, mapping python Object to MySQL Relational Table, then we can Create, Update, Delete database via python script on the backend of server side.
MySQL is run on back-end as database server.
FLASK is used role as API on server.
HTML, CSS, JAVASCRIPT are used to compose a webpage, either static or dynamic pages.


## 4. Challenge statement
In the database structure, it includes Many-to-Many relation between employees table and todos table, in python, it is Employee class and Todo Class, because of Class, we can make its instance object to map with table, but EmployeeTodo is a table that mapping Many to Many between Employees and Todos, it is a method or attribute of Employee class. It is challenge on me for the complicated relationship between the tables.


## 5. Risks
The project is a complete system, it requires a lot of work, it can add more and more features to make the app to do more things. But in the first set up, I will design the table simplest, make the app work at the first time is my first goal. After that, feel free to add more and more features to it.

## 6. Infrastructure
The App will run on Virtual Machine environment for building code base and testing, map the host port to guest port, RESTful Api, Web Flask, Web dynamic run on guest virtual machine as micro webapp server, host machine run as client, use browser to request page on server( guest machine). After testing, make sure the The app work functionally, then it will deploy to internet, make the site alive to public,  post to GitHub repository as well.

## 7. Existing Solutions
The good news is: Holberton School has current project AirBnB_Clone, it is a big project for the students in Holberton School, it took 4 months to do parts by parts.  This App structure learn from AirBnB_Clone project. And will add user login validation feature and browser terminal to manipulate backend database.



## Author
Bill Huang

## License
MIT License
