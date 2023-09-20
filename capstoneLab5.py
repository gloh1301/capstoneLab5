"""
A menu - you need to add the database and fill in the functions.
"""

# TODO create database table OR set up Peewee model to create table

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')


def search_by_name():
    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')


def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?')


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?')


if __name__ == '__main__':
    main()