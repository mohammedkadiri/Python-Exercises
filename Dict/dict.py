# student = {'name': 'John', 'age':25, 'courses': ['Math','CompSci']}
#
# for key,value in student.items():
#     print(key,value)
#
# def info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# info(19,{'name':'james'}, (1,2,3,4))

# dic = {'one': 1, 'b': 'bee'}
# dic.update({'two': 2})
#
# for key, value in dic.items():
#     print(dic[key])
#
# if 'one' in dic:
#     del dic['one']
# print(dic)

# for key in sorted(dic):
#     print(key, dic[key])

# 1. Write a Python program to sort (ascending and descending) a dictionary by value.
# import operator
#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
# print('Original dictionary: ', d)
# sorted_desc = sorted(d.items(), key= operator.itemgetter(0))
# print('Dictionary in ascending order by value : ',sorted_desc)
# sorted_asc= sorted(d.items(), key=operator.itemgetter(0), reverse=True)
# print('Dictionary in descending order by value : ',sorted_asc)

# 2 Write a Python script to add a key to a dictionary.
# sample =  {0: 10, 1: 20}
#
# sample.update({2: 30})
#
# print(sample)

# 3 Write a Python script to concatenate following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# dict4 = {}
# for x in (dic1,dic2,dic3):
#     dict4.update(x)
# print(dict4)

# 4 Write a Python script to check if a given key already exists in a dictionary

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(5)
# is_key_present(9)

# 5 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

#sample = dict()
#
# def temp(n):
#     for x in range(1, n+1):
#         sample[x] = x * x
#     print(sample)
# temp(5)

# 6 Program to merge to dictionaries

# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
#
# d = d1.copy()
# d.update(d2)
# print(d)

# 7 Program to  sum all items in a dictionary

# sum = 0
# dict = {1: 1, 2: 2, 3: 3, 4: 4}
#
# for key, values in dict.items():
#     sum += dict[key]
# print(sum)

# 9. Write a Python program to iterate over dictionaries using for loops
# d = {1:5, 2:2, 3:3, 4:4}
#
# for x,y in d.items():
#     print(x, y)

# 11. Write a Python program to multiply all the items in a dictionary
# d = {1: 5, 2: 2, 3: 3, 4: 4}
# mul = 1
# for x,y in d.items():
#     mul *= y
# print(mul)

# 12. Write a Python program to remove a key from a dictionary.
#
# d = {1: 5, 2: 2, 3: 3, 4: 4}
#
# if 1 in d:
#     del d[1]
# print(d)

# 13. Write a Python program to map two lists into a dictionary.
#
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
#
# t = tuple(zip(l1,l2))
# print(dict(t))

# 14. Write a Python program to sort a dictionary by key
# d = {1: 5, 2: 2, 3: 3, 4: 4, 0: 0, 6: 6, 5: 5}
#
# for key in sorted(d):
#     print(key, d[key])

# 15. Write a Python program to get the maximum and minimum value in a dictionary.

# my_dict = {'x':500, 'y':5874, 'z': 560}
# print(max(my_dict.values()))
# print(min(my_dict.values()))

