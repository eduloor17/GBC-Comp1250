#Task5-Determine if the year is a leap year and output the result
year = int(input("Enter a year: "))
if year % 4 == 0: #step 1, go to step2
    if year % 100 == 0: #step 2, go to step3
        if year % 400 == 0: #step3, go to step4
            print(f"Yes, {year} is a leap year.") #(year has 366 days, step3 -> year%400==0)
        else:
            print(f"No, {year} is not a leap year.") #(year has 365 days, step3 -> year%400!=0)
    else:
        print(f"Yes, {year} is a leap year.") #(year has 366 days, step2 -> year%100!=0)
else:
    print(f"No, {year} is not a leap year.") #(year has 365 days, step1 -> year%4!= 0)
