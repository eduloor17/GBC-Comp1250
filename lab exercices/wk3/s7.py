dow = input("enter the day of the week: ")
tod = int(input("enter the time of the dat: "))

#if dow == "Monday":
if dow.lower().startswith("fri") or dow == "5" or dow[0]=="5":
    if tod >= 9 and tod <= 11:
        print("COMP1250")
    elif tod >= 11 and tod <= 13:
            print("Networking")
    else:
            print("Go home")
elif dow.lower().startswith("mon"):
    if tod >= 9 and tod <= 11:
        print("COMP1250")
else:
    print("Go home weekend")