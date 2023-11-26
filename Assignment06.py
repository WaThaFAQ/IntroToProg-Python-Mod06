# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Jason Noumeh,11/26/2023,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Data ----------------------------------------------- #
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # hold the choice made by the user.


# Processing ----------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    JNoumeh,11/25/2023,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
         This method opens the json file and loads the pre-existing data
         to the "student_data" list parameter, then closes the file. The json
         module is used to load the data.

        The method is carried out using exception blocks which calls to a function
        handling error message if the file does not exist or catch all error. The
        function handling errors are defined in the IO class.

         ChangeLog: (Who, When, What)
         JNoumeh,11/25/2023,Created Method
         """
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
        """
        This method opens the json file and writes the parameter student_data
        to the file. The json module is used to dump the data into the file.

        The method is carried out using exception blocks which calls to a function
        handling error message if the file does not exist or catch all error. The
        function handling errors are defined in the IO class.

        ChangeLog: (Who, When, What)
        JNoumeh,11/25/2023,Created Method
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    JNoumeh,11/25/2023,Created Class
    JNoumeh,11/25/2023,Added menu output and input functions
    JNoumeh,11/25/2023,Added a function to display the data
    JNoumeh,11/25/2023,Added a function to display custom error messages
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user.

        ChangeLog: (Who, When, What)
        JNoumeh,11/25/2023,Created method

        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This method prints the menu to the user.

        ChangeLog: (Who, When, What)
        JNoumeh,11/25/2023,Created Method
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This method collects the users choice after being presented the menu and
        assigns it to the variable choice and returns the value to the main
        module.

        ChangeLog: (Who, When, What)
        JNoumeh,11/25/2023,Created Method
        """
        choice: str = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This method gets triggered when the user chooses option 1 which collects
        the students first, last and course name from the user. These values are
        then appended to the variable student_data which contains initial data.

        ChangeLog: (Who, When, What)
        JNoumeh,11/25/2023,Created Method
        """
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
         This method gets triggered when the user chooses option 2 which then outputs
         the data stored in the variable students to the user. This variable contains
         both data from a pre-existing file and user defined data.

         ChangeLog: (Who, When, What)
         JNoumeh,11/26/2023,Created Method
         """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}')
        print('-' * 50)


# When the program starts, read the file data into a list of dictionaries (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,student_data=students)


# Present and Process the data
while True:  # Will continue the iterative process indefinitely

    # Presents user with menu of options
    IO.output_menu(menu=MENU)

    # Stores user menu choice
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Registers a student for a course
        IO.input_student_data(student_data=students)
        continue
    if menu_choice == "2":  # Show current data
        IO.output_student_courses(student_data=students)
        continue
    if menu_choice == "3":  # save data to file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    if menu_choice == "4":  # exits program
        break




