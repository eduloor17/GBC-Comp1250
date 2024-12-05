# This is a module that I will use in task5
# This module is going to create 2 functions for save the student information, and get the information
my_id = "101503932"
my_name = "Eduardo"
my_lastname = "Loor"


def students(student_id, first_name, last_name):
    with open("StudentInformation-GBC.txt", 'w') as file:

        file.write(f"{student_id}\n{first_name}\n{last_name}")


def info(student_id, first_name, last_name):
    welcome_message = f"Welcome {first_name} {last_name} to George Brown College!!"
    #print(welcome_message)
    students(student_id, first_name, last_name)
    return welcome_message


def main():
    global my_id, my_name, my_lastname
    return info(my_id, my_name, my_lastname)


if __name__ == "__main__":
    main()
