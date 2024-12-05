daily_schedule = {
        "Monday": {
            "Cisco-Class": "9-11 am",
            "Python-Class": "11-1 pm",
            "COMP2000": "3-5pm"
        },
        "Friday": {
            "Python-Class": "9-11 am",
            "Cisco-Class": "11-1 pm"
        }
}
print(daily_schedule)
#ask my classmate if they have the same class
for x in daily_schedule:
    print(x)
    print(daily_schedule[x])
    print("Do you have class on", daily_schedule.keys())
    answer = input("Enter your Class:")
    if answer in daily_schedule[x]['Cisco-Class']:
        print("we have the same class")
    else:
        print("we do not have same class")
