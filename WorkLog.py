import os


def display_main_menu():
    os.system('clear')
    print("\t______Work Log Main Menu______")
    # As a user of the script, I should be prompted with a menu to
    # choose whether to add a new entry or lookup previous entries.
    print("Please enter a letter from the choices below")
    print("[A]dd a new entry")
    print("[L]ookup previous entries")
    print("[Q]uit application")


def display_find_menu():
    os.system('clear')
    print("\t______Work Log Find Menu______")
    # As a user of the script, if I choose to find a previous entry,
    # I should be presented with four options: find by xxx
    print("Please enter a letter from the choices below")
    print("Find by [D]ate")
    print("Find by [T]ime spent")
    print("Find by [E]xact search")
    print("Find by [P]attern")
    print("[R]eturn to Main Menu")


choice = ''
display_main_menu()
while choice != 'q':
    choice = input().lower()
    # Respond to the user's choice.
    if choice == 'a':
        print("You chose to add a new entry")
    elif choice == 'l':
        print("You chose to lookup a new entry")


"""Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.

As a user of the script, if I choose to enter a new work log, I should be able to provide a task name, a number of minutes spent working on it, and any additional notes I want to record.


Note:

    When finding by date, I should be presented with a list of dates with entries and be able to choose one to see entries from.
    When finding by time spent, I should be allowed to enter the number of minutes a task took and be able to choose one to see entries from.
    When finding by an exact string, I should be allowed to enter a string and then be presented with entries containing that string in the task name or notes.
    When finding by a pattern, I should be allowed to enter a regular expression and then be presented with entries matching that pattern in their task name or notes.



Menu has a “quit” option to exit the program.
Entries can be deleted and edited, letting user change the date, task name, time spent, and/or notes.
Entries can be searched for and found based on a date range. For example between 01/01/2016 and 12/31/2016.
Entries are displayed one at a time with the ability to page through records (previous/next/back).
"""