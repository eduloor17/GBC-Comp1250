"""
make decision
    if <boolean expression>:
        statement if expression is true
    elseif <boolean expression>:
        statement if expression is true
    else statement if expression is False

"""
age = int(input("Enter your age: "))
category = ""
# determinate their age category
    if age <= 4 and age >= 0:
        category = "Baby"
    elif age <= 12:
        category = "child"
    elif age <= 18:
        category = "teen"
    elif age <= 65:
        category = "adult"
    else
        category = "elder"