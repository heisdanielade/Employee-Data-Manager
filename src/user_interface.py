"""
    FILENAME: utils.py
    This file contains program for the user interface which is used 
    to perform actions on the Database.
"""


from database import DatabaseActions
from utils import tabulate_data

# Class containing function(s) for possible user actions
class UserActions:
    @staticmethod
    def main():
        print("\n\n----------------------WELCOME----------------------\n")
        print("(i) Kindly select which action you would like to perform.\n"
              "\n- Type 'all' to get a list of all employee data"
              "\n- Type 'add' to add new employees"
              "\n- Type 'edit' to edit an existing employee's data"
              "\n- Type 'all-sort' or 'all-sort-id' to get list of employees sorted by ID"
              "\n- Type 'all-sort-sal' to get list of employees sorted by salary"
              "\n- Type 'show-info' to show data for a certain employee"
              "\n- Type 'update-all' to update a certain data for all employees"
              "\n- Type 'delete-emp' to delete an employee"
              "\n- OR Type 'exit' to stop the code.\n")


        # check user input and match to designated function
        while True:
            user_action = input("\n-> ACTION: ").strip().lower()
            if user_action == 'add':
                # handle incorrect input type error
                try:
                    number_of_people = int(input("\n>> How many employees to add: \n- "))
                    DatabaseActions.add_data(number_of_people)
                except ValueError as e:
                    print("\n(e) ERROR: Please enter a number.\n")
            elif user_action == 'edit':
                employee_data = DatabaseActions.read_data()
                DatabaseActions.edit_employee(employee_data)
            elif user_action in ['all', 'all-sort', 'all-sort-id', 'all-sort-sal']:
                employee_data = DatabaseActions.read_data()
                if user_action == 'all-sort' or user_action == 'all-sort-id':
                    employee_data = sorted(employee_data, key=lambda x: x['id'])
                elif user_action == 'all-sort-sal':
                    employee_data = sorted(employee_data, key=lambda x: x['salary'])
                tabulate_data(employee_data)
            elif user_action == 'show-info':
                employee_data = DatabaseActions.read_data()
                DatabaseActions.show_info(employee_data)
            elif user_action == 'update-all':
                    DatabaseActions.update_all(employee_data)
            elif user_action == 'delete-emp':
                    DatabaseActions.delete_employee(employee_data)
            elif user_action == 'exit':
                break
            else:
                print("\n(i) INFO: Kindly enter a valid action.")


if __name__ == "__main__":
    UserActions.main()

