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
    # def __init__(self, data, number_of_people):
    #     self.data = data
    #     self.number_of_people = number_of_people

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
    def add_data(number_of_people):
        employee_data = DatabaseActions.read_data()
        for _ in range(number_of_people):
            time_created = datetime.now().strftime("%d/%b/%y %H:%M:%S") 
            employee_id = random.randint(12468, 92680)
            first_name = input("\n>> FIRST NAME: \n- ") 
            last_name = input(">> LAST NAME: \n- ")
            birth_date = input(">> BIRTH DATE (dd/mm/yy): \n- ")
            email = input(">> EMAIL: \n- ")
            phone_number = input(">> TELEPHONE: \n- ")  
            home_address = input(">> HOME ADDRESS: \n- ")
            emergency_contact_info = input(">> EMERGENCY CONTACT: \n- ")
            pesel_number = input(">> PESEL NUMBER: \n- ")
            job_title = input(">> JOB TITLE: \n- ")
            department = input(">> DEPARTMENT: \n- ")
            employment_date = input(">> EMPLOYMENT DATE (dd/mm/yy): \n- ")
            employment_status = input(">> EMPLOYMENT STATUS: \n- ") 
            clearance_level = input(">> CLEARANCE LEVEL: \n- ") 
            salary = input(">> MONTHLY SALARY: \n- ")
            try:
                salary = float(salary)
            except ValueError as e:
                # Handle the case where the conversion fails
                salary = '--'
            last_modified = '--'

            employee_data.append({
                'created_at': time_created,
                'id': employee_id,
                'first_name': first_name,
                'last_name': last_name,
                'birth_date': birth_date,
                'email': email,
                'phone_number': phone_number,
                'home_address': home_address,
                'emergency_contact_info': emergency_contact_info,
                'pesel_number': pesel_number,
                'job_title': job_title,
                'department': department,
                'employment_date': employment_date,
                'employment_status': employment_status, 
                'clearance_level': clearance_level, 
                'salary': salary,
                'last_modified': last_modified
            })
        DatabaseActions.store_data(employee_data)
        print("\n (s) STATUS: Employee data saved successfully.\n")

    # function to reorder keys in the db table
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
                'birth_date': employee.get('birth_date'),
                'email': employee.get('email'),
                'phone_number': employee.get('phone_number'),
                'home_address': employee.get('home_address'),
                'emergency_contact_info':employee.get('emergency_contact_info'),
                'pesel_number':employee.get('pesel_number'),
                'job_title':employee.get('job_title'),
                'department':employee.get('department'),
                'employment_date':employee.get('employment_date'),
                'employment_status':employee.get('employment_status'), 
                'clearance_level':employee.get('clearance_level'), 
                'salary': employee.get('salary'),
                'last_modified': employee.get('last_modified')
            }
            reordered_data.append(reordered_employee)
        
        DatabaseActions.store_data(reordered_data)
        print("\n(s) STATUS: All employee data reordered successfully.\n")

    # function to allow user to update the value of a particular key for all employees in the database
    @staticmethod
    def update_all(employee_data):
        key_to_update = input("\n-> KEY TO UPDATE: ")
        new_value = input("-> VALUE: ")
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
        try:
            employee_id = int(input("\n-> Enter the ID of the employee you want to edit: "))
        except ValueError as e:
            print("\n(e) ERROR: Invalid Employee ID.\n")
        found = False
        try:
            for emp in employee_data:
                    if emp['id'] == employee_id:
                        # if id is found then print the employee's current data
                        found = True
                        print("\n-> Current Data:")
                        tabulate_data([emp])
                        emp['first_name'] = input(">> FIRST NAME (leave blank to keep current): ") or emp['first_name']
                        emp['last_name'] = input(">> LAST NAME (leave blank to keep current): ") or emp['last_name']
                        emp['birth_date'] = input(">> BIRTH DATE (dd/mm/yy) (leave blank to keep current): ") or emp['birth_date']
                        emp['email'] = input(">> EMAIL (leave blank to keep current): ") or emp['email']
                        emp['phone_number'] = input(">> TELEPHONE (leave blank to keep current): ") or emp['phone_number']
                        emp['home_address'] = input(">> HOME ADDRESS (leave blank to keep current): ") or emp['home_address']
                        emp['emergency_contact_info'] = input(">> EMERGENCY CONTACT (leave blank to keep current): ") or emp['emergency_contact_info']
                        emp['pesel_number'] = input(">> PESEL NUMBER (leave blank to keep current): ") or emp['pesel_number']
                        emp['job_title'] = input(">> JOB TITLE (leave blank to keep current): ") or emp['job_title']
                        emp['department'] = input(">> DEPARTMENT (leave blank to keep current): ") or emp['department']
                        emp['employment_date'] = input(">> EMPLOYMENT DATE (dd/mm/yy) (leave blank to keep current): ") or emp['employment_date']
                        emp['employment_status'] = input(">> EMPLOYMENT STATUS (leave blank to keep current): ") or emp['employment_status']           
                        emp['clearance_level'] = input(">> CLEARANCE LEVEL (leave blank to keep current): ") or emp['clearance_level']           
                        new_salary = input(">> MONTHLY SALARY (leave blank to keep current): ")
                        if new_salary:
                            emp['salary'] = float(new_salary)
                        emp['last_modified'] = datetime.now().strftime("%d/%b/%y %H:%M:%S") 
                        break
        except Exception as e:
            return e
        if found:
            DatabaseActions.store_data(employee_data)
            print("\n(s) STATUS: Employee data updated successfully.\n")
        else:
            print("\n(s) STATUS: Employee data not found.\n")

    # function show info of a particular employee based on ID
    @staticmethod
    def show_info(employee_data):
        try:
            employee_id = int(input("\n-> Enter Employee ID: "))
        except ValueError as e:
            print("\n(e) ERROR: Invalid Employee ID.\n")
        found = False
        try:
            for emp in employee_data:
                    if emp['id'] == employee_id:
                        # if id is found then print the employee's current data
                        found = True
                        print("\n-> EMPLOYEE DATA:")
                        tabulate_data([emp]) 
        except Exception as e:
            return e
        if found:
            DatabaseActions.store_data(employee_data)
            print("\n(s) STATUS: Employee data retrieved successfully.\n")
        else:
            print("\n(s) STATUS: Employee data not found.\n")


    # function to edit employee data by selecting the employee's ID
    @staticmethod
    def delete_employee(employee_data):
        try:
            employee_id = int(input("\n-> Enter the ID of the employee you want to delete: "))
        except ValueError:
            print("\n(e) ERROR: Invalid Employee ID.\n")
            return
        found = False
        index_to_remove = None
        for index, emp in enumerate(employee_data):
            if emp['id'] == employee_id:
                found = True
                print("\n-> Current Data:")
                tabulate_data([emp])
                option = input("\n>> Are you sure you want to delete this employee? (yes/no): ").strip().lower()
                if option == "yes":
                    index_to_remove = index
                elif option == "no":
                    print("\n(s) STATUS: Operation cancelled.\n")
                    return
                else:
                    print("\n(i) Invalid input.\n")
                    return
                break
        if found and index_to_remove is not None:
            employee_data.pop(index_to_remove)
            print("\n(s) STATUS: Employee data deleted successfully.\n")
            DatabaseActions.store_data(employee_data)  # Assuming this function handles storage correctly.
        elif not found:
            print("\n(s) STATUS: Employee data not found.\n")

