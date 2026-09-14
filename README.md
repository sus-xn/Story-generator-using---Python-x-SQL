# Personalized Story Generator

It is a basic project using Python and an SQL database. While everyone is doing the same repetitive projects, such as hospital management, hotel management, or the usual “blah, blah, blah,” I took this a little further by generating stories using per-written templates and user input.

![image](https://github.com/sus-xn/Story-generator-using---Python-x-SQL/blob/main/SQL-things%20you%20need!/images/Screenshot%202026-09-14%20130543.png?raw=true)

Disclaimer: This project has its own drawbacks and limitations. Do not expect the output to be like an AI-generated story. The application generates stories from predefined templates and replaces their placeholders with user-provided information. The quality and variety of the generated stories therefore depend on the templates available in the database.

## Project Overview

Personalized Story Generator is a Command Line Interface (CLI) application developed using Python 3.6 and MySQL.

The purpose of the project is to generate a simple personalized story based on information entered by the user, such as:

Name \
Place \
Item

The application uses predefined story templates stored in a MySQL database. A template contains placeholders such as {name}, {place}, and {item}. Python replaces these placeholders with the user's input and produces the final personalized story.

The project also includes CRUD operations for managing story templates, user inputs, and generated stories.



## Prerequisites

Before you begin, ensure you have met the following requirements to run this project:

- Python 3.6
- MySQL [database]
- MySQL connector [ use this command to install : pip install mysql-connector-python ]


## SQL database setup

Create a fresh new databsae named "story_generator" and then inside the database create 3 tables to store, update and delete. First table is "story_templates" to store the templates with an unique id for generate stories. Second tables is "user_inputs" to store the values of "name","place","item" while user endering for generating new story. And the third table is "generated_stories" to store generated stories with its timestamp.The SQL commands and values are in "[SQL-things you need](https://github.com/sus-xn/Story-generator-using---Python-x-SQL/tree/main/SQL-things%20you%20need!)" folder.

## Python setup

Install python and setup as usually and remember to install SQL-Python connector on your system. and then test the connector using this code in a new file.\
![image](https://github.com/sus-xn/Story-generator-using---Python-x-SQL/blob/main/SQL-things%20you%20need!/images/Screenshot%202026-09-14%20124850.png?raw=true) \
If the connection is estabilshed successfully the output shows like this : \
![image](https://github.com/sus-xn/Story-generator-using---Python-x-SQL/blob/main/SQL-things%20you%20need!/images/connection%20established.png?raw=true) \

## HI
