"""
    FILENAME: database.py
    This file contains program for performing CRUD operations on the database.
"""

import json
from datetime import datetime
import random
from utils import tabulate_data


# File where employee data is stored
filename = "db.txt"

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


    # function to add new employee data to the text file
    @staticmethod
    def add_employees(number_of_people):
        employee_data = DatabaseActions.read_data()
        for _ in range(number_of_people):
            first_name = input("\n>> FIRST NAME: \n- ") 
            last_name = input(">> LAST NAME: \n- ")
            email = input(">> EMAIL: \n- ") # -----PENDING---
            age = input(">> AGE: \n- ")
            salary = input(">> MONTHLY SALARY: \n- ")
            try:
                salary = float(salary)
            except ValueError as e:
                # Handle the case where the conversion fails
                salary = '--'
            time_created = datetime.now().strftime("%d/%b/%y %H:%M:%S")
            employee_id = random.randint(12468, 92680)
            employee_data.append({
                'created_at': time_created,
                'id': employee_id,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'age': age,
                'salary': salary
            })
        DatabaseActions.store_data(employee_data)
        print("\n (s) STATUS: Employee data saved successfully.\n")

    @staticmethod
    def reorder_keys():
        employee_data = DatabaseActions.read_data()
        reordered_data = []
        for employee in employee_data:
            reordered_employee = {
                'created_at': employee.get('created_at'),
                'id': employee.get('id'),
                'first_name': employee.get('first_name'),
                'last_name': employee.get('last_name'),
                'email': employee.get('email'),
                'age': employee.get('age'),
                'salary': employee.get('salary')
            }
            reordered_data.append(reordered_employee)
        
        DatabaseActions.store_data(reordered_data)
        print("\n(s) STATUS: All employee data reordered successfully.\n")


    # function to allow user to update the value of a particular key for all employees in the database
    @staticmethod
    def update_all(employee_data):
        key_to_update = input("\n-> KEY TO UPDATE: ")
        new_value = input("-> VALUE FOR KEY: ")
    
        employee_data = DatabaseActions.read_data()
        updated = False
        for employee in employee_data:
            # Check if the "key_to_update" is missing or empty in the employee dictionary
            if key_to_update not in employee or not employee[key_to_update]:
                employee[key_to_update] = new_value  # Set a default or placeholder 
                updated = True
            elif key_to_update in employee:
                employee[key_to_update] = new_value # Set a default or placeholder 
                updated = True

        if updated:
            DatabaseActions.store_data(employee_data)
            print(f"\n(s) STATUS: Data for all employees updated successfully.\n")
            DatabaseActions.reorder_keys() # Re-order the newly added key in the user interface table
        else:
            print(f"\n(i) INFO: No update needed. All employees already have this data.\n")


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
                tabulate_data([emp])
                emp['first_name'] = input(">> FIRST NAME (leave blank to keep current): ") or emp['first_name']
                emp['last_name'] = input(">> LAST NAME (leave blank to keep current): ") or emp['last_name']
                emp['email'] = input(">> EMAIL (leave blank to keep current): ") or emp['email']
                new_age = input(">> AGE (leave blank to keep current): ")
                if new_age:
                    emp['age'] = int(new_age)
                new_salary = input(">> MONTHLY SALARY (leave blank to keep current): ")
                if new_salary:
                    emp['salary'] = float(new_salary)
                break
        if found:
            DatabaseActions.store_data(employee_data)
            print("\n (s) STATUS: Employee data updated successfully.\n")
        else:
            print("\n (s) STATUS: Employee data not found.\n")


