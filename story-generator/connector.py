import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "#Pass123",
        database = "story_generator")


print(connect_db())
