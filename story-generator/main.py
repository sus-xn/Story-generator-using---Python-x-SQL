from story_generation import *
from view import *
from create import *
from update import *
from delete import *

def main_menu():
    while True:
        print("-----------------------------------")
        print("}   STORY GENERATOR - MAIN MENU   {")
        print("-----------------------------------")
        print("|  1. Generate a new story.       |")
        print("|  2. View past stories.          |")
        print("|  3. View story templaes.        |")
        print("|  4. View user inputs.           |")
        print("|  5. Add a new story template.   |")
        print("|  6. Update a story template.    |")
        print("|  7. Delete a story template.    |")
        print("|  8. Delete user input data.     |")
        print("|  9. Delete a past story.        |")
        print("|  10. Exit.                      |")
        print("-----------------------------------")
        opt = input("|> Choose an option (1-12): ")

        if opt == '1':
            generate_story()
        elif opt == '2':
            view_past_stories()
        elif opt == '3':
            view_templates()
        elif opt == '4':
            view_user_inputs()
        elif opt == '5':
            create_story_template()
        elif opt == '6':
            update_story_template()
        elif opt == '7':
            delete_story_template()
        elif opt == '8':
            delete_user_input()
        elif opt == '9':
            delete_past_story()
        elif opt == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()