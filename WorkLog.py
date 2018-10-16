import os
import csv
import datetime

def show_menu_header(header):
    os.system('clear')
    print("______Work Log {}______".format(header))

def main_menu():
    # As a user of the script, I should be prompted with a menu to
    # choose whether to add a new entry or lookup previous entries.
    show_menu_header("Main Menu")
    choice = input("""Please enter a letter from the choices below
[A]dd a new entry
[L]ookup previous entries
[Q]uit application
>""").lower()
    return choice


def run_main_menu():
    choice = ''
    while choice != 'q':
        choice = main_menu()
        if choice == 'a':
            print("You chose to add a new entry")
            create_new_entry()
            break
        elif choice == 'l':
            print("You chose to lookup a new entry")
            #display_find_menu()
            display_entries()
            break
        elif choice == 'q':
            print("We are sorry to see you go, goodbye.")
        else:
            print("You did not enter a valid choice, please only enter letters from the list")


def display_find_menu():
    # As a user of the script, if I choose to find a previous entry,
    # I should be presented with four options: find by xxx
    choice = ''
    while choice != 'r':
        show_menu_header("Find Menu")
        choice = input("""Please enter a letter from the choices below
Find by [D]ate
Find by [T]ime spent
Find by [E]xact search
Find by [P]attern"
[R]eturn to Main Menu
>""").lower()
        if choice == 'd':
            print("You chose to search by date")
        elif choice == 't':
            print("You chose to lookup by time spent")
        elif choice == 'e':
            print("You chose to lookup by exact search")
        elif choice == 'p':
            print("You chose to lookup by pattern")
        elif choice == 'r':
            print("You chose to return to the main menu")
            run_main_menu()
        else:
            print("You did not enter a valid choice, please only enter letters from the list")


def create_new_entry():
    # As a user of the script, if I choose to enter a new work log, I should be able to provide a task name, a number of
    # minutes spent working on it, and any additional notes I want to record.
    show_menu_header("Add New Entry")
    #Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
    while True:
        task_title = input("What is your task title?>")
        if not task_title:
            print("task title is not optional, please enter it")
            continue
        else:
            break
    while True:
        try:
            minutes_spent = int(input("How many minutes did you spend?>"))
        except ValueError:
            print("Please input an integer amount of minutes")
            continue
        else:
            break
    notes = input("Please enter any optional notes>")
    with open('workLog_records.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.date.today().strftime("%m/%d/%Y"), task_title, minutes_spent, notes])
    run_main_menu()


def display_entries():
    # When displaying the entries, the entries should be displayed in a readable format with the date, task name, time
    # spent, and notes information.
    # Entries are displayed one at a time with the ability to page through records (previous/next/back).
    choice = ''
    while choice != 'r':
        show_menu_header("Display Entries")
        print("The first entry is blah blah")
        choice = input("""Please enter a letter from the choices below
[E]dit current record
[N]ext record
[P]revious record
[R]eturn to Main Menu
>""").lower()
        if choice == 'e':
            print("You chose to edit")
        elif choice == 't':
            print("You chose go to the next record")
        elif choice == 'e':
            print("You chose go to the previous record")
        elif choice == 'r':
            print("You chose to return to the main menu")
            run_main_menu()
        else:
            print("You did not enter a valid choice, please only enter letters from the list")


if __name__ == "__main__":
    run_main_menu()



"""

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