from connector import *
from view import *

#--------------------------------------------------------------------------------------------------------

def update_story_template():
    temp = view_templates()
    db = connect_db()
    cursor = db.cursor()
    if temp == 0:
        try:
            template_id = int(input("Enter the ID of the template you want to update: "))
        except ValueError:
            print("\nNumbers only accept as ID.\n")
            return
    
        cursor.execute("SELECT id FROM story_templates")
        ids = cursor.fetchall()
    
        for (i,) in ids:
            if template_id == i:
                new_template = input("\nEnter the new template text: ")
                cursor.execute("UPDATE story_templates SET template_text = %s WHERE id = %s",(new_template, template_id))
                db.commit()
                print("\n>>> Story template updated successfully. <<<\n")
                break
        else:
            print("\n>>> Invalid template ID. <<<\n")
    elif temp == 1:
        print(">>> No templates available to update. <<<\n")
            
  
    cursor.close()
    db.close()

#--------------------------------------------------------------------------------------------------------