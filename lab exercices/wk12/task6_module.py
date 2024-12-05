# This is a module that I will use in task6
# This search module is going to open the file that I create at task5 and then
# searches for a student by either their student_number, student_firstname or last name


import os


def read_student_information(filename):
    """Read student data from the specified file and return as a list of dictionaries."""
    students = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Process lines in chunks of 3
            for i in range(0, len(lines), 3):
                if i + 2 < len(lines):  # Ensure there are enough lines for ID, firstname, and lastname
                    student_id = lines[i].strip()
                    firstname = lines[i + 1].strip()
                    lastname = lines[i + 2].strip()
                    students.append({
                        "id_number": student_id,
                        "firstname": firstname,
                        "lastname": lastname
                    })
    return students


def search_by_number(student_id):
    students = read_student_information("StudentInformation-GBC.txt")
    for student in students:
        if student["id_number"] == student_id:
            print(f"Student found: {student}")
        elif student["id_number"] != student_id:
            print(f"Sorry. Student ID: {student_id} is not found.")
    return


def search_by_firstname(student_firstname):
    students = read_student_information("StudentInformation-GBC.txt")
    for student in students:
        if student["firstname"].lower() == student_firstname.lower():
            print(f"Student found: {student}")
        elif student["firstname"].lower() != student_firstname.lower():
            print(f"Sorry. Student Firstname: {student_firstname} is not found.")
    return


def search_by_lastname(student_lastname):
    students = read_student_information("StudentInformation-GBC.txt")
    for student in students:
        if student["lastname"].lower() == student_lastname.lower():
            print(f"Student found: {student}")
        elif student["lastname"].lower() != student_lastname.lower():
            print(f"Sorry. Student Lastname: {student_lastname} is not found.")
    return


def search_student():
    """Ask the user which field to search and call the appropriate search function."""
    print("If you want to search by ' Student ID (1) - Firstname (2) - Lastname (3) '\n")
    option = input("Please - Choose from 1 to 3: ")

    if option == "1":
        student_id = input("Student ID: ")
        search_by_number(student_id)
    elif option == "2":
        student_firstname = input("Student Firstname: ")
        search_by_firstname(student_firstname)
    elif option == "3":
        student_lastname = input("Student Lastname: ")
        search_by_lastname(student_lastname)
    else:
        print("Invalid search field. Try again!")


def main():
    flag = False
    while not flag:
        search_student()
        question = input("Search again (YES/yes , Y/y  or NO/no , N/n): ").lower()
        if question == "no" or question == "n":
            flag = True


if __name__ == "__main__":
    main()
