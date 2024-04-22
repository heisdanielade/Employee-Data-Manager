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
            first_name = input("\n-> FIRST NAME: \n- ") 
            last_name = input("-> LAST NAME: \n- ")
            # email = input("-> EMAIL: \n- ") # -----PENDING---
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
                tabulate_data([emp])
                emp['first_name'] = input("-> FIRST NAME (leave blank to keep current): ") or emp['first_name']
                emp['last_name'] = input("-> LAST NAME (leave blank to keep current): ") or emp['last_name']
                new_age = input("-> AGE (leave blank to keep current): ")
                if new_age:
                    emp['age'] = int(new_age)
                new_salary = input("-> MONTHLY SALARY (leave blank to keep current): ")
                if new_salary:
                    emp['salary'] = float(new_salary)
                break
        if found:
            DatabaseActions.store_data(employee_data)
            print("\n (s) STATUS: Employee data updated successfully.\n")
        else:
            print("\n (s) STATUS: Employee data not found.\n")


