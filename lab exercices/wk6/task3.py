#Create my dictionaty with 3 element or key
gyeinfo = {
    "city": "Guayaquil",
    "independence_year": 1820,
    "country": "Ecuador"
}
print(f"The city where I born: {gyeinfo["city"]}") #Get one value from the keys
print(f"This is my dictionary with one value {gyeinfo}")
gyeinfo.pop("independence_year") # remove one of the key from my dictionary.
i = 0
for key, value in gyeinfo.items():
    i= i + 1
    print(f"My {i} key is '{key}' equal to '{value}'")
