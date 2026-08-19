from connector import *

def generate_story():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM story_templates")
    result = cursor.fetchone()
    temp = result[0]
    if temp == 0:
        print("\n>>> No story templates available. \nPlease add a template before generating a story.\n")
    elif temp > 0:
        name = input("Enter a name: ")
        place = input("Enter a place: ")
        item = input("Enter an item: ")
        cursor.execute("INSERT INTO user_inputs (name, place, item) VALUES (%s,%s,%s)",(name,place,item))
        db.commit()

        cursor.execute("SELECT template_text FROM story_templates ORDER BY RAND() LIMIT 1")
        template = cursor.fetchone()[0]

        story = template.format(name=name, place=place, item=item)
        print("\n-> Here is your personalized story: \n")
        print(story)

        cursor.execute("INSERT INTO generated_stories (story) VALUES (%s)",(story,))
        db.commit()
    cursor.close()
    db.close()