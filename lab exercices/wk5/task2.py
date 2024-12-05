shopping = ["Rice", "Chicken", "Canola Oil"]
print(f"My list of 3 items to buy: {shopping}")
additem = input("Enter an shopping item to add: ")
shopping.append(additem) #add the item by taking the value of additem
print(f"My list of 4 items to buy(after add 1): {shopping}")
shopping.pop(0) # removing my index 0 from my list
print(f"My list of 3 items to buy(after remove index 0): {shopping}")
#determine if an item exists in the my shopping list
item = input("Enter an item to determinate wherever exists or not in my shopping list: ")
if item in shopping:
    # -if it does, display its index
    print(f"{item} is at index {shopping.index(item)}")
else:
    # -if it does not, give user message
    print(f"{item} is not in the list. My list is {shopping}")