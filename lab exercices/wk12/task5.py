# This program is going to import mymodule and then the information that
# the user enter will save on the "StudentID-GBC.txt" file that I have in the module

import task5_module

student_id = input("Please I need your Student number or Student ID: ")
firstname = input("Could you tell me your firstname: ")
lastname = input("Last question - Provide your last name: ")
print(task5_module.info(student_id=student_id, first_name=firstname, last_name=lastname))
print("The following variables are from my module")
print(f"Student Id: {task5_module.my_id}")
print(f"Student firstname: {task5_module.my_name}")
print(f"Student lastname: {task5_module.my_lastname}")
