
# -----------PROJECT DETAILS------------
"""
    Adetunji Daniel Adediran - 114083 - UZ
    A program that creates a database in a text file which stores user's
      data with the ability to modify and sort data based on required arguments.
"""


# Handle possible module or import error
try:
    from datetime import datetime
    from tabulate import tabulate
    import random, json
except (ModuleNotFoundError, ImportError) as e:
    print(f"\n\n(e) ERROR: {e}\n\n")



employee_data = []

filename = "db.txt"


# all actions that can be performed by the user on the database
class UserActions:
    print("\n----------------------WELCOME----------------------\n")
    print("(i) Kindly select which action you would like to perform."
              "\n- Type 'add' to add new employees"
              "\n- Type 'all' to get list of all employee data"
              "\n- Type 'all-sort-age' to get list of employees sorted by age"
              "\n- Type 'all-sort-sal' to get list of employees sorted by salary"
              "\n- OR Type 'exit' to stop the code.")
    

    def main():
        while True:
            user_action = input("\n-> ACTION: ")
            
            # perform action based on user input
            if user_action == 'add':
                number_of_people = int(input("\nHow many employees to add: \n- "))
                DatabaseActions.main(number_of_people, filename)
            elif user_action == 'all':
                DatabaseActions.get_data(employee_data)
            elif user_action == 'all-sort-age':
                DatabaseActions.sort_data_by_age(employee_data)
            elif user_action == 'all-sort-sal':
                DatabaseActions.sort_data_by_salary(employee_data)
            elif user_action == 'exit':
                break
            else:
                print("\n(i) Kindly enter a valid action.")


# all actions that can be performed on database
class DatabaseActions:
    @staticmethod
    def store_data(data, database):
        with open(filename, "w") as database:
            # save data to file
            json.dump(data, database)
            print("\n\n(s) STATUS: Data saved successfully.\n\n")
    
    @staticmethod
    def tabulate_data(data):
        try:
            # Better formatted headers for the table
            raw_header = [{'Created At':'', 'ID':'', 'First Name':'', 'Last Name':'', 'Age':'', 'Salary':''}]
            header = raw_header[0].keys()
            rows = [x.values() for x in data]
            data_table = tabulate(rows, header)
            print(data_table)
        except ValueError as e:
            print(f"\n(e) ERROR: {e}\n")
        else:
            print("\n\n(s) STATUS: Data received successfully.\n\n")

    @staticmethod
    def get_data(employee_data):
        DatabaseActions.tabulate_data(employee_data)
    
    def main(number_of_people, filename):
        number_of_people = number_of_people

        # function to handle invalid inputs from user
        def get_input(prompt):
            while True:
                try:
                    user_input = int(input(prompt))
                    return user_input  # Return the input if it's successfully converted to an integer
                except ValueError as e:
                    print(f"\n\n(e) ERROR: {e}\n")
                    print("(i) Kindly enter a valid input.\n")

        for i in range(number_of_people):
            # get user data
            first_name = input("\n-> FIRST NAME {}: \n- ".format(i+1)) 
            last_name = input("-> LAST NAME {}: \n- ".format(i+1))
            age = get_input("-> AGE {}: \n- ".format(i+1))
            salary = get_input("-> MONTHLY SALARY {}: \n- ".format(i+1))

            # generate time properties in database
            raw_time = datetime.now()
            time_created = raw_time.strftime("%d/%b/%y %H:%M:%S")

            employee_id = random.randint(12468, 92680)
            
            # store data in dictionary then save to employee list
            person = {
                'created_at':time_created,
                'id': employee_id,
                'first_name': first_name,
                'last_name': last_name,
                'age': age,
                'salary': salary  
            }
            employee_data.append(person)
        

        print("---Confirming data---")
        print(f"\n{employee_data}\n")
        print(f"\nFile path: {filename}\n")
        DatabaseActions.store_data(employee_data, filename)

        
    def sort_data_by_age(employee_data):
        print("\n[----Data sorted by AGE----]\n")
        sorted_employee_list = sorted(employee_data, key = lambda x: x['age'])

        # Print the sorted list
        DatabaseActions.tabulate_data(sorted_employee_list)


    def sort_data_by_salary(employee_data):
            print("\n[----Data sorted by SALARY----]\n")
            sorted_employee_list = sorted(employee_data, key = lambda x: x['salary'])

            # Print the sorted list
            DatabaseActions.tabulate_data(sorted_employee_list)


if __name__ == "__main__":
    user = UserActions
    # db = DatabaseActions
 
    user.main()
    # db.main()
    # db.get_data(employee_data)
    # db.sort_data_by_age(employee_data)
else:
    print("(i) An error occured...")




