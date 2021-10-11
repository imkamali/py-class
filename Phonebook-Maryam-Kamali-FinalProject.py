import sqlite3, sys

class Phonebook(object):
    def __init__(self):
        try:
            c.execute('CREATE TABLE entries(id INTEGER PRIMARY KEY, name TEXT, phone TEXT unique)')
        except:
            pass
        print('Welcome to the Phonebook. This is a training project for pyclass -SEMATEC- 00-04-24 - Maryam Kamali.')


    def add_entry():
        name = input('Please enter a name: ')
        number = input('Please enter a phone number: ')
        c.execute('INSERT INTO entries(name, phone) VALUES(?,?)', (name, number))

    def del_entry():
        name = input('Please enter a name to delete: ')
        c.execute('DELETE FROM entries WHERE name=?', (name,))

    def rollback():
        db.rollback()

    def querylist():
        c.execute('SELECT name, phone FROM entries')
        for items in c:
            print(items)
    
    def queryname():
        name = input('Please enter a name to search: ')
        c.execute('SELECT name,phone FROM entries where name=?', (name,))
        for items in c:
            print(items)
    
    def queryphone():
        phone = input('Please enter a phone number to search: ')
        c.execute('SELECT name,phone FROM entries where phone=?', (phone,))
        for items in c:
            print(items)

    def save():
        db.commit()

    def exit():
        sys.exit()

class MainMenu(Phonebook):
    def __init__(self):
        print('''
Main Menu
Please select an option:
    1. "add" - to add an entry.
    2. "delete" - to delete an entry.
    3. "rollback" - to undo your last change.
    4. "querylist" - to query an entry.
    5. "queryname" - to search by name(return name and phone).
    6. "queryphone" - to search by phone(return name and phone).
    7. "save" - to save changes.
    8. "exit" - to exit the program.
            ''')

        selection = input()
        if selection == 'add':
            
            try:
                Phonebook.add_entry()
            except:
                print('Phone Number already exists.')

        if selection == 'delete':
            Phonebook.del_entry()

        if selection == 'rollback':
            Phonebook.rollback()

        if selection == 'querylist':
            Phonebook.querylist()
        
        if selection == 'queryname':
            Phonebook.queryname()
            
        if selection == 'queryphone':
            Phonebook.queryphone()

        if selection == 'save':
            Phonebook.save()

        if selection == 'exit':
            print("You left the phone book. You can run the program again for reuse.")
            Phonebook.exit()
            

db = sqlite3.connect('phonebookDB.sqlite')
c = db.cursor()

Phonebook()
while True:
    MainMenu()

db.close()