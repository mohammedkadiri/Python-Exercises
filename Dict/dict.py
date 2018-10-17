#Empty dictionary
dict = {}
print(dict)

# Get a value by a key in a dictionary
dict = {"Name": "Joe", "Age": 19, "Height": 1.80}
print(dict["Name"], dict["Height"])
print(dict.get("Age"))

# Add a key/value to dict
dict["DOB"] = "19 July 1999"
print(dict)

#Iterate over python dictionary
for key, value in dict.items():
    print(key, " : ", dict[key])