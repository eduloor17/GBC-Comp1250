list = []
for i in range(5):
    while True:
        newlist = input(f"Enter the {i+1}th Input:")
        if newlist in list:
            print(f"This input is repeated.")
        else:
            list.append(newlist)
            break
print(f"My List with 5 things: {list}")