# Extracting the first letter of each item in the listofWords
listOfWords = ["this","is","a","list","of","words"]

# List comprehension

new_list = [word[0] for word in listOfWords]

print(new_list)

# Converting each item in the alphabet list to lower case
alphabet = ["A", "B", "C"]

alphabet = [item.lower() for item in alphabet]

print(alphabet)

# Extract numbers from a string

string = "Hello 12345 World"

numbers = [item for item in string if item.isdigit()]

print(numbers)