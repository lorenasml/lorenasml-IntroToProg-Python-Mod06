# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# Change Log: (Who, When, What)
#   Lorena,11/16/2024,Created Script
#   Lorena, 11/18/2024, Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        global students
        global file

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except KeyError as e:
            print("Please make sure your dictionary key exists!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:  # catch all
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
            if file.closed == False:
                file.close()
        print("The following students have been successfully enrolled:")
        with open(FILE_NAME, "r") as file:
            for row in file:
                print(row.strip())

class IO:

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        global MENU

        print(MENU)

    @staticmethod
    def input_menu_choice():
        global menu_choice

        choice = input("Enter your menu choice number: ")
        return choice

    @staticmethod
    def input_student_data(student_data: list):

        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Which course are you enrolled in? ")
            student_data = {"student_first_name": student_first_name,
                            "student_last_name": student_last_name,
                            "course_name": course_name}
            students.append(student_data)
        except ValueError as e:
            print(e)  # Prints the custom message
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:  # catch-all
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")

    @staticmethod
    def output_student_courses(student_data: list):
        global students

        print("-" * 50)
        print(students)
        print("-" * 50)
        for student in students:
            print(f"{student["student_first_name"]}, {student["student_last_name"]}, {student["course_name"]}")
        print("-" * 50)

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break  # out of the while loop