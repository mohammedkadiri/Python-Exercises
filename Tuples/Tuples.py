# 1. Write a Python program to create a tuple.
# tuple = (1,2,3)
# print(tuple)
# 2. Write a Python program to create a tuple with different data types
# tuple = (30,'String', 1, [1,2,3])
# print(tuple)
#3. Write a Python program to create a tuple with numbers and print one item.
# tuple = (1,2,3)
# tuple = 1,
# print(tuple)
#4. Write a Python program to unpack a tuple in several variables.
# tuptle = (1,2,3,'hi')
# n1, n2, n3, n4 = tuple
# print(n1, n2, n3, n4)
#5. Write a Python program to add an item in a tuple.
# t = (1,2,3)
# t = t + (4,)
# print(t)
#6 Write a Python program to convert a tuple to a string.
# tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# str =  ''.join(tuple)
# print(str)
# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.
# t = tuple(range(1,9))
# fourth = t[3]
# last = t[-4]
# print(fourth, last)
# 9. Write a Python program to find the repeated items of a tuple.
# t = (1,2,3,4,2,3,4,6,5)
# l  = [i for i in t if t.count(i) > 1]
# l = set(l)
# print(list(l))
# 10. Write a Python program to check whether an element exists within a tuple
# element = input("Enter a element to search: ")
# tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print(element in tuplex)
#  11. Write a Python program to convert a list to a tuple
# print(tuple([1,2,3,4]))
#  12. Write a Python program to remove an item from a tuple.
# t = (1,2,3,4)
# l = list(t)
# l.remove(2)
# print(tuple(l))
# 13. Write a Python program to slice a tuple
# t = tuple(range(1,11))
# t = t[4:]
# print(t)
# 14. Write a Python program to find the index of an item of a tuple.
# t = (1,"hi", 1.2, "blue")
# print(t.index("hi"))
# # 15. Write a Python program to find the length of a tuple
# print(len((1,2,3,4,5,6)))
# 16. Write a Python program to convert a tuple to a dictionary
# t = (("England", "London"), ("Ireland", "Dublin"))
# d = dict((x,y) for x, y in t)
# print(d)
# 17. Write a Python program to unzip a list of tuples into individual lists.
# l = [(1, 2), (3, 4), (8, 9)]
# print(list(zip(*l)))
# 18. Write a Python program to reverse a tuple.
# t = (1,2,3,4)
# print(tuple(reversed(t)))
# 19. Write a Python program to convert a list of tuples into a dictionary.
# t = [("color", "orange"), ("food", "burger"), ("sport","football")]
# print(dict(t))
# 20. Write a Python program to print a tuple with string formatting.
# t = (100, 200, 300)
# print("This is a tuple {0}".format(t))
