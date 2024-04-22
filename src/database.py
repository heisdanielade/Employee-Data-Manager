"""
    FILENAME: database.py
    This file contains program for performing CRUD operations on the database.
"""

import json
from datetime import datetime
from tabulate import tabulate
import random


# File where employee data is stored
filename = "db.txt"


# Class containing function(s) for possible user actions
class UserActions:
    @staticmethod
    def main():
        print("\n----------------------WELCOME----------------------\n")
        print("(i) Kindly select which action you would like to perform.\n"
              "\n- Type 'add' to add new employees"
              "\n- Type 'all' to get a list of all employee data"
              "\n- Type 'edit' to edit an existing employee's data"
              "\n- Type 'all-sort-age' to get list of employees sorted by age"
              "\n- Type 'all-sort-sal' to get list of employees sorted by salary"
              "\n- OR Type 'exit' to stop the code.")


        # check user input and match to designated function
        while True:
            user_action = input("\n-> ACTION: ").lower()
            if user_action == 'add':
                number_of_people = int(input("\nHow many employees to add: \n- "))
                DatabaseActions.add_employees(number_of_people)
            elif user_action == 'edit':
                employee_data = DatabaseActions.read_data()
                DatabaseActions.edit_employee(employee_data)
            elif user_action in ['all', 'all-sort', 'all-sort-age', 'all-sort-sal']:
                employee_data = DatabaseActions.read_data()
                if user_action == 'all-sort-age' or user_action == 'all-sort':
                    employee_data = sorted(employee_data, key=lambda x: x['age'])
                elif user_action == 'all-sort-sal':
                    employee_data = sorted(employee_data, key=lambda x: x['salary'])
                DatabaseActions.tabulate_data(employee_data)
            elif user_action == 'exit':
                break
            else:
                print("\n(i) Kindly enter a valid action.")


# Class containing function(s) for actions that can be performed on the database
class DatabaseActions:
    # function to store the employee data in the designated file
    @staticmethod
    def store_data(data):
        with open(filename, "w") as db:
            json.dump(data, db)


    # function to read the employee data from the text file
    @staticmethod
    def read_data():
        try:
            with open(filename, "r") as db:
                return json.load(db)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    # function to tabulate the employee data for a more presentable interface
    @staticmethod
    def tabulate_data(data):
        headers = ['Created At', 'ID', 'First Name', 'Last Name', 'Age', 'Salary']
        table = [list(emp.values()) for emp in data]
        print(tabulate(table, headers=headers, tablefmt='grid'))


    # function to add new employee data to the text file
    @staticmethod
    def add_employees(number_of_people):
        employee_data = DatabaseActions.read_data()
        for _ in range(number_of_people):
            first_name = input("\n-> FIRST NAME: \n- ") 
            last_name = input("-> LAST NAME: \n- ")
            age = int(input("-> AGE: \n- "))
            salary = float(input("-> MONTHLY SALARY: \n- "))
            time_created = datetime.now().strftime("%d/%b/%y %H:%M:%S")
            employee_id = random.randint(12468, 92680)
            employee_data.append({
                'created_at': time_created,
                'id': employee_id,
                'first_name': first_name,
                'last_name': last_name,
                'age': age,
                'salary': salary
            })
        DatabaseActions.store_data(employee_data)
        print("\n (s) STATUS: Employee data saved successfully.\n")


    # function to edit employee data by selecting the employee's ID
    @staticmethod
    def edit_employee(employee_data):
        employee_id = int(input("\n-> Enter the ID of the employee you want to edit: "))
        found = False
        for emp in employee_data:
            if emp['id'] == employee_id:
                # if id is found then print the employee's current data
                found = True
                print("\n-> Current Data:")
                DatabaseActions.tabulate_data([emp])
                emp['first_name'] = input("-> Enter new first name (leave blank to keep current): ") or emp['first_name']
                emp['last_name'] = input("-> Enter new last name (leave blank to keep current): ") or emp['last_name']
                new_age = input("-> Enter new age (leave blank to keep current): ")
                if new_age:
                    emp['age'] = int(new_age)
                new_salary = input("-> Enter new salary (leave blank to keep current): ")
                if new_salary:
                    emp['salary'] = float(new_salary)
                break
        if found:
            DatabaseActions.store_data(employee_data)
            print("\n (s) STATUS: Employee data updated successfully.\n")
        else:
            print("\n (s) STATUS: Employee data not found.\n")


if __name__ == "__main__":
    UserActions.main()


