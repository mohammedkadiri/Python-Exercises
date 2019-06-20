# poem = open("C:\\Users\Mo\Documents\Python-Exercises\Files\poem.txt", 'r')
#
# for line in poem:
#     print(line, end='')
#
# poem.close()

# with open("C:\\Users\Mo\Documents\Python-Exercises\Files\poem.txt", 'r') as poem:
#     lines = poem.readlines()
#     text = "".join(lines).replace("\n", " ")
#     print(text)

# cities = ["London", "Manchester", "Dublin", "Lisbon", "Tokyo"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)