"""
    FILENAME: user_interface.py
    This file contains program for the user interface which is used 
    to perform actions on the Database.
"""


import time
from database import DatabaseActions
from utils import tabulate_data


# Class containing function(s) for possible user actions
class UserActions:
    def main():
        print("\n\n---------------- EMPLOYEE DATA MANAGEMENT SYSTEM ----------------\n")
        print("\n+ Welcome, type 'help' to see a list of possible commands.\n")

        # check user input and match to designated function
        while True:
            user_action = input("\n-> ACTION: ").strip().lower()
            if user_action == 'help':
                UserActions.help()
            elif user_action == 'add-emp':
                # handle incorrect input type error
                try:
                    number_of_people = int(input("\n>> How many employees to add: \n- "))
                    DatabaseActions.add_data(number_of_people)
                except ValueError as e:
                    print("\n(e) ERROR: Please enter a number.\n")
            elif user_action == 'edit-emp':
                employee_data = DatabaseActions.read_data()
                DatabaseActions.edit_employee(employee_data)
            elif user_action in ['all', 'sort-id', 'sort-salary']:
                employee_data = DatabaseActions.read_data()
                if user_action == 'sort-id':
                    employee_data = sorted(employee_data, key=lambda x: x['id'])
                elif user_action == 'sort-salary':
                    employee_data = sorted(employee_data, key=lambda x: x['salary'])
                tabulate_data(employee_data)
            elif user_action == 'get-total':
                employee_data = DatabaseActions.read_data()
                DatabaseActions.get_total(employee_data)
            elif user_action == 'show-info':
                employee_data = DatabaseActions.read_data()
                DatabaseActions.show_info(employee_data)
            elif user_action == 'update-all':
                    DatabaseActions.update_all(employee_data)
            elif user_action == 'delete-emp':
                    DatabaseActions.delete_employee(employee_data)
            elif user_action == 'exit':
                time.sleep(0.5)
                print("\n(i) Program ended!\n")
                break
            else:
                print("\n(e) ERROR: Kindly enter a valid action.")

    def help():
        print("\n(i) These are currently available commands:\n"
              "\n--DISPLAY--"
              "\n   all               Get a list of all employee data"
              "\n   show-info         Show data for a certain employee"
              "\n   get-total         Show the total number of employees"
        
              "\n\n--UPDATE--"
              "\n   add-emp           Add new employees"
              "\n   edit-emp          Edit an existing employee's data"
              "\n   delete-emp        Delete an employee"
              "\n   update-all        Update a certain data for all employees"
 
              "\n\n--SORT--"
              "\n   sort-id           Get list of employees sorted by ID"
              "\n   sort-salary       Get list of employees sorted by salary"
              "\n   exit              Stop the program\n")

if __name__ == "__main__":
    UserActions.main()

