#My sport store
#Create a dictionary of your inventory - The inventory should have 3 categories -Each category should have 2 items
myinventory = {
    "soccer": {
        "shoes_men": 26,
        "shoes_women": 10
    },
    "Pickleball": {
        "Paddle": 15,
        "Net": 3
    },
    "Camping": {
        "sleeping bag": 9,
        "tent": 7
    }
}
#You need to select a vendor
#Create a dictionary of the vendor's inventory-The inventory should have 3 categories- Each category should have 2 items
vendor_inventory = {
    "soccer": {
        "Gloves": 70,
        "shoes_women": 125
    },
    "Pickleball": {
        "Paddle": 8,
        "Balls": 41
    },
    "Camping": {
        "Table(3ftx2ft)": 27,
        "Mat": 16
    }
}
#Output the items that YOU have but the VENDOR does not have
print("My store stock when the Vendor does not have the same:")
i = 0
for my_category, my_items in myinventory.items():
    for item in my_items:
        if item not in vendor_inventory.get(my_category, {}):
            i = i + 1
            print(f"{i}.- {my_category}: {item}")
#Output the items that BOTH YOU and the VENDOR have
print("\nItems that my store and Vendor have:")
s = 0
#for vendor_category, vendor_items in vendor_inventory.items():
#    for item in vendor_items:
#        if item in myinventory.get(vendor_category, {}):
#            s += 1
#            print(f"{s}.-  {vendor_category}: {item}")
for my_category, my_items in myinventory.items():
    for item in my_items:
        if item in vendor_inventory.get(my_category, {}):
            s += 1
            print(f"{s}.-  {my_category}: {item}")
#Ask the user for an item
search_item = input("\nEnter the product that you want: ")
#Determine if the item is in STOCK (you have it)
#Determine if vendor carries the item (vendor has it)
my_stock = 0
vendor_stock = 0
for my_category, my_items in myinventory.items():
    if search_item in my_items:
        my_stock = 1
        break
for vendor_category, vendor_items in vendor_inventory.items():
    if search_item in vendor_items:
        vendor_stock = 1
        break
if my_stock:
    print(f"\nMy store has {search_item} in stock.")
else:
    print(f"\nMy store did not have {search_item} in stock.")
if vendor_stock:
    print(f"The vendor has {search_item} in stock.")
else:
    print(f"The vendor does not have {search_item} in stock.")