# Personalized Story Generator

It is a basic project using Python and an SQL database. While everyone is doing the same repetitive projects, such as hospital management, hotel management, or the usual “blah, blah, blah,” I took this a little further by generating stories using per-written templates and user input.

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
