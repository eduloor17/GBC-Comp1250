import re
#Task 1 - Create the following variables:
print("Task 1 - Creating the following variables: ")
text = " "
number = 1000
username = "admin"
userid = 12345
password = "a8e3l6$#"
email = "ex@ex.ex"
print(text, number, username, userid, password, email)
#Task 2 - Write the regular expression that will match the variable text
# content with an empty string
#Only text will match with an empty string
#text = "D"
t2 = re.match("^ $", text)
if t2:
    print("Task 2 - match with an empty string in text", text)
else:
    print("Task 2 - no match with text: ", text)

#Task 3 - Write the regular expression that will match the variable text
# content that has at least 10 characters
#text = "abcde12345"
#text = "task3"
t3 = re.match(".{10,}", text)
if t3:
    print("Task 3 - match with text at least 10 characters: ", text)
else:
    print("Task 3 - no match with text: ", text)

#Task 4 - Write the regular expression that will match the variable text
# with only non-alphanumerical characters.
#text only match with empty space
#text = "text4"
t4 = re.match(r"^\W+$", text)
if t4:
    print("Task 4 - match with text: ", text)
else:
    print("Task 4 - no match with text: ", text)

#Task 5 - Write the regular expression that will match the variable username
# with: Only alphabetical characters and underscores
# match is the username = "admin_gbc" but no match username = admin$
#username = "admin_gbc"
t5 = re.match("^[a-zA-Z_]+$", username)
if t5:
    print("Task 5 - match. With username: ", username)
else:
    print("Task 5 - no match. With username: ", username)

#Task 6 - Write the regular expression that will match the variable userid
# with only numeric characters
# match is the userid = numbers but no match userid = 12345.67
#userid = 12345.67
t6 = re.match(r"^\d+$", str(userid))
if t6:
    print("Task 6 - match. With userid: ", userid)
else:
    print("Task 6 - no match. With userid: ", userid)
#Task 7 - Write the regular expression that will match the variable password with:
#At least 1 number - At Least 1 alphabetic character - At Least 1 special character (!”#$%&/)
#password = "age31!"
t7 = re.match("^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!\"#$%&/]).{8,}$", password)
if t7:
    print("Task 7 - The password match. Password: ", password)
else:
    print("Task 7 - The password does not match. Password: ", password)

#Task 8 - Write the regular expression that will match the variable email with a valid email.
# Please note that a valid email includes: At Least 1 alphabetic character before the at symbol
#Exactly 1 at symbol - At Least 1 alphabetic character after the at symbol - Exactly 1 period symbol
#At Least 1 alphabetic character after the period symbol
#This email does not match "17eduloor@live.com", but "eduloor17@live.com" match!
#email = "17eduloor@live.com"
t8 = re.match(r"^[a-zA-Z]+[0-9]+@[a-zA-Z]+\.[a-zA-Z]+$", email)
if t8:
    print("Task 8 - The email match. Email: ", email)
else:
    print("Task 8 - The email does not match. Email: ", email)
