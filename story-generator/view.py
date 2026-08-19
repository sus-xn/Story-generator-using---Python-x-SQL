from connector import *

#--------------------------------------------------------------------------------------------------------

def view_templates():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, template_text FROM story_templates")
    templates = cursor.fetchall()
    check_T = 0
    if templates:
        print("\nStory Templates: \n")
        for template in templates:
            print(f"ID: {template[0]}, Template: {template[1]}\n")
    else:
        print("\n>>> No templates found. <<<\n")
        check_T = 1
    cursor.close()
    db.close()
    return check_T

#--------------------------------------------------------------------------------------------------------

def view_past_stories():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, story, created_at FROM generated_stories ORDER BY created_at DESC")
    stories = cursor.fetchall()
    check_S = 0
    if stories:
        print("\nPast Stories: \n")
        for idx, (story_id, story, created_at) in enumerate(stories, 1):
            print(f"{idx}. (ID: {story_id}) - {created_at}:")
            print(story)
            print("-"*40)
    else:
        print("\n>>> No past stories found. <<<\n")
        check_S = 1
    cursor.close()
    db.close()
    return check_S

#--------------------------------------------------------------------------------------------------------

def view_user_inputs():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, place, item FROM user_inputs")
    inputs = cursor.fetchall()
    check_I = 0
    if inputs:
        print("\nUser Inputs: \n")
        for input_data in inputs:
            print(f"ID: {input_data[0]}, Name: {input_data[1]}, Place: {input_data[2]}, Item: {input_data[3]}")
    else:
        print("\n>>> No user input found. <<<\n")
        check_I = 1
    cursor.close()
    db.close()
    return check_I

#--------------------------------------------------------------------------------------------------------