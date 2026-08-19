from connector import *
from view import *

#--------------------------------------------------------------------------------------------------------

def delete_story_template():
    temp=view_templates()
    db = connect_db()
    cursor = db.cursor()
    if temp == 0:
        try:
            template_id = int(input("Enter the ID of the template you want to delete: "))
        except ValueError:
            print("\n>>> Numbers only accept as ID. <<<")
            return
    
        cursor.execute("SELECT id FROM story_templates")
        ids = cursor.fetchall()

        for (i,) in ids:
            if template_id == i:
                cursor.execute("DELETE FROM story_templates WHERE id = %s",(template_id,))
                db.commit()
                print("\n>>> Story template deleted successfully. <<<\n")
                break
        else:
            print("\n>>> Invalid template ID. <<<") 
    elif temp == 1:
        print(">>> No templates available to delete. <<<\n")   
    
    cursor.close()
    db.close()

#--------------------------------------------------------------------------------------------------------

def delete_user_input():
    u_temp = view_user_inputs()
    db = connect_db()
    cursor = db.cursor()
    if u_temp == 0:
        try:
            input_id = int(input("Enter the ID of the user input you wnat to delete: "))
        except ValueError:
            print("\n>>> Number only accept as ID. <<<")
            return
    
        cursor.execute("SELECT id FROM user_inputs")
        inid = cursor.fetchall()

        for (i,) in inid:
            if input_id == i:
                cursor.execute("DELETE FROM user_inputs WHERE id = %s",(input_id,))
                db.commit()
                print("\n>>> User input deleted successfully. <<<\n")
                break
        else:
            print("\n>>> Invalid input ID. <<<\n")
    elif u_temp == 1:
        print(">>> No user input available to delete. <<<\n")
 
    cursor.close()
    db.close()

#--------------------------------------------------------------------------------------------------------

def delete_past_story():
    s_temp = view_past_stories()
    db = connect_db()
    cursor = db.cursor()
    if s_temp == 0:
        try:
            story_id = int(input("Enter the ID of the story you wnat to delete: "))
        except ValueError:
            print("\n>>> Number only accept as ID. <<<")
            return
    
        cursor.execute("SELECT id FROM generated_stories")
        sid = cursor.fetchall()

        for (i,) in sid:
            if story_id == i:
                cursor.execute("DELETE FROM generated_stories WHERE id = %s",(story_id,))
                db.commit()
                print("\n>>> Past story deleted successfully. <<<\n")
                break
        else:
            print("\n>>> Invalid story ID. <<<\n")
    elif s_temp == 1:
        print(">>> No past stories available to delete. <<<\n")

    cursor.close()
    db.close()

#--------------------------------------------------------------------------------------------------------