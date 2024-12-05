print("Guess Game! Number is more than 25 and less than 100. I will tell you how many guesses you try")
tried = 1
while True:
    number = int(input("Input the number: "))
    if 50 <= number <= 75:
        #if the user guess, display congrats
        print(f"Congrats! You have tried: {tried} times")
        break
    else:
        tried += 1
        print("Invalid number. Please try again.")