import os
import csv
import datetime
import re

WORK_LOG_FILE = 'workLog_records.csv'
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
            display_find_menu()
            #display_entries()
            break
        # Menu has a “quit” option to exit the program.
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
Find by [P]attern
[R]eturn to Main Menu
>""").lower()
        if choice == 'd':
            # print("You chose to search by date")
            display_entries("d")
        elif choice == 't':
            # print("You chose to lookup by time spent")
            display_entries("t")
        elif choice == 'e':
            # print("You chose to lookup by exact search")
            display_entries("e")
        elif choice == 'p':
            # print("You chose to lookup by pattern")
            display_entries("p")
        elif choice == 'r':
            # print("You chose to return to the main menu")
            run_main_menu()
        else:
            print("You did not enter a valid choice, please only enter letters from the list")


def create_new_entry():
    # As a user of the script, if I choose to enter a new work log, I should be able to provide a task name, a number of
    # minutes spent working on it, and any additional notes I want to record.
    show_menu_header("Add New Entry")
    entry_information = gather_entry_information(False)
    with open(WORK_LOG_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(entry_information)
    run_main_menu()


def overwrite_work_log(new_entry_information):
    with open(WORK_LOG_FILE, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["date", "task_title", "minutes", "notes"])
        for entry in new_entry_information:
            writer.writerow([entry["date"], entry["task_title"], str(entry["minutes"]), entry["notes"]])


def gather_entry_information(includeDate):
    date_str = datetime.date.today().strftime("%m/%d/%Y")
    if includeDate:
        while True:
            try:
                date_str = input("What is your date?>")
                datetime.datetime.strptime(date_str, '%m/%d/%Y')
            except ValueError:
                print("Incorrect data format, should be MM/DD/YYYY")
                continue
            else:
                break
    # Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
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
    return [date_str, task_title, minutes_spent, notes]



def load_work_log(search_type):
    all_work_logs = []
    with open(WORK_LOG_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            all_work_logs.append({"date": row["date"], "task_title": row["task_title"],
                                  "minutes": row["minutes"], "notes": row["notes"], "show_log": 1})
    # for log in all_work_logs:
    # print(log["date"] + " " + str(log["show_log"]))
    if search_type == 'd':
        while True:
            try:
                date_str = input("For which MM/DD/YYYY date(s) do you want to search? (enter two separated by a space"
                                 " if you want a range)>")
                split_date_str = date_str.split()
                if len(split_date_str) == 2:
                    date1 = datetime.datetime.strptime(split_date_str[0], '%m/%d/%Y')
                    date2 = datetime.datetime.strptime(split_date_str[1], '%m/%d/%Y')
                    # print("The first date is " + split_date_str[0])
                    # print("The second date is " + split_date_str[1])
                    for log in all_work_logs:
                        log["show_log"] = 1
                        log_date = datetime.datetime.strptime(log["date"], '%m/%d/%Y')
                        if date1 < date2:
                            # print("date1 is earlier than date2 " + log["date"] + " " + str(log_date < date1) + " " + str(log_date > date2))
                            if log_date < date1 or log_date > date2:
                                log["show_log"] = 0
                        elif date2 < date1:
                            # print("date1 is later than date2 " + log["date"] + " " + str(log_date < date2) + " " + str(log_date > date1))
                            if log_date < date2 or log_date > date1:
                                log["show_log"] = 0
                        else:
                            # print("dates are equal, log date is " + log["date"] + " " + str(log_date != date1))
                            if log_date != date1:
                                log["show_log"] = 0

                else:
                    only_date = datetime.datetime.strptime(date_str, '%m/%d/%Y')
                    # print("The only date is " + date_str)
                    for log in all_work_logs:
                        log["show_log"] = 1
                        log_date = datetime.datetime.strptime(log["date"], '%m/%d/%Y')
                        # print("log date is " + log["date"] + " " + str(log_date != only_date))
                        if log_date != only_date:
                            log["show_log"] = 0
            except ValueError:
                print("Incorrect data format, should be MM/DD/YYYY")
                continue
            else:
                break
                # for log in all_work_logs:
                # print(log["date"] + " " + str(log["show_log"]))
    elif search_type == 't':
        while True:
            try:
                search_minutes = int(input("For how many minutes do you want to search?>"))
                for log in all_work_logs:
                    log["show_log"] = 1
                    if int(log["minutes"]) != search_minutes:
                        log["show_log"] = 0
            except ValueError:
                print("Please input an integer amount of minutes")
                continue
            else:
                # for log in all_work_logs:
                #     print(log["minutes"] + " " + str(log["show_log"]))
                break
    elif search_type == 'e':
        search_exact = input("What is your exact search string?>")
        for log in all_work_logs:
            log["show_log"] = 1
            if log["task_title"] != search_exact and log["notes"] != search_exact:
                log["show_log"] = 0
        # for log in all_work_logs:
        #     print(log["task_title"] + " " + log["notes"] + " " + str(log["show_log"]))

    elif search_type == 'p':
        search_pattern = input("What is your pattern (regex) search string?>")
        for log in all_work_logs:
            log["show_log"] = 1
            if not re.search(search_pattern, log["task_title"]) and not re.search(search_pattern, log["notes"]):
                log["show_log"] = 0
        # for log in all_work_logs:
        #  print(log["task_title"] + " " + log["notes"] + " " + str(log["show_log"]))
    return all_work_logs


def display_entries(search_type):
    # When displaying the entries, the entries should be displayed in a readable format with the date, task name, time
    # spent, and notes information.
    work_logs = load_work_log(search_type)
    choice = ''
    i = 0
    while choice != 'r':
        # Entries are displayed one at a time with the ability to page through records (previous/next/back).
        print("i: " + str(i) + " len(work_logs) " + str(len(work_logs)))
        if (i < len(work_logs) and i >= 0):
            log = work_logs[i]

        if log["show_log"]:
            show_menu_header("Display Entries")
            print("Date: {} \nTask Title: {} \nMinutes Spent: {} \nNotes(Optional): {}"
                .format(log["date"], log["task_title"], str(log["minutes"]), log["notes"]))
            choice = input("""What would like you like to do? [E]dit record / [D]elete record / [N]ext record / [P]revious record / [R]eturn to Main Menu>""").lower()
        #Entries can be deleted and edited, letting user change the date, task name, time spent, and/or notes.
        if choice == 'e':
            print("You chose to edit")
            edited_entry_information = gather_entry_information(True)
            log["date"] = edited_entry_information[0]
            log["task_title"] = edited_entry_information[1]
            log["minutes"] = edited_entry_information[2]
            log["notes"] = edited_entry_information[3]
        elif choice == 'd':
            if len(work_logs) == 1:
                print("You can't delete the last log")
            else:
                # print("You chose go to delete the record")
                work_logs.remove(log)
        # Entries are displayed one at a time with the ability to page through records (previous/next/back).
        elif choice == 'n':
            # print("You chose go to the next record")
            if i == len(work_logs):
                i = 0
            else:
                i += 1
        elif choice == 'p':
            # print("You chose go to the previous record")
            if i == 0:
                i = len(work_logs)
            else:
                i -= 1
        elif choice == 'r':
            # print("You chose to return to the main menu")
            overwrite_work_log(work_logs)
            run_main_menu()
        else:
            print("You did not enter a valid choice, please only enter letters from the list")


if __name__ == "__main__":
    run_main_menu()

