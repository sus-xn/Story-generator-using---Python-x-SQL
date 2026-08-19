import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "<your SQL password>",
        database = "story_generator")


print(connect_db())
