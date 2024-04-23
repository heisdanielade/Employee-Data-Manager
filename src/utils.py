"""
    FILENAME: utils.py
    This file contains utility functions that are used across 
    multiple modules within this project.
"""

from tabulate import tabulate


# function to tabulate the employee data for a more presentable interface
@staticmethod
def tabulate_data(data):
    headers = ['Created At', 'ID', 'First Name', 'Last Name', 'Email', 'Age', 'Salary']
    table = [list(emp.values()) for emp in data]
    print(tabulate(table, headers=headers, tablefmt='grid'))