from connector import *

def create_story_template():
    template = input("Enter the new story template (use {name}, {place}, {item} as placeholders): ")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO story_templates (template_text) VALUES (%s)",(template,))
    db.commit()
    print("\nNew story template added successfully.")
    cursor.close()
    db.close()
    
#--------------------------------------------------------------------------------------------------------