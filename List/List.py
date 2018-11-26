# 1. Write a Python program to sum all the items in a list
# numbers = [1,2,3,4]
# total = 0
# for x in numbers:
#     total += x
# print(total)
# 2. Write a Python program to multiplies all the items in a list.
# total = 1
# for x in numbers:
#     total *= x
# print
#3. Write a Python program to get the largest number from a list
# print(max(numbers))
#4. Write a Python program to get the smallest number from a list.
# print(min(numbers))
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# sample = ['abc','xyz','aba','1221']
# count = 0
# for index in sample:
#     if len(index) >= 2:
#         temp = list(index)
#         if temp[0] == temp[-1]:
#             count += 1
#
# print("count: " + str(count))
#7. Write a Python program to remove duplicates from a list
# sample = [1,2,4,1,2,4,5,3,5,6,2]
# print(set(sample))
#8. Write a Python program to check a list is empty or not
# a = []
# if not a:
#     if not a:
#         print("list is empty")
# else:
#     print("list is not empty")
# 9. Write a Python program to clone or copy a list
# sample = [1,2,4,5]
#  copy = sample.copy()
#  print(copy)
# 10. Write a python program to find the list of words that are longer than n

# def long_words(n, str):
#     txt = str.split(" ")
#     word = [x for x in txt if len(x) > n]
#     return word
#
# print(long_words(3, "The woman said hello to the man across the street"))

# 11  Write a Python function that takes two lists and returns True
# if they have at least one common member

# def compare(list_one, list_two):
#     result = False
#     for i in list_one:
#         for j in list_two:
#             if i == j:
#                 result = True
#                 return result
#
# print(compare(['hi', '1' , 'mom'],  ['1' , '2' ,'3', '5']))

# 12 Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
#
# print(color)
# 13 Write a Python program to print the numbers of a specified list after removing even numbers from it.
# numbers = list(range(0, 10))
#
# odd = [x for x in numbers if x % 2 != 0]
#
# print(odd)

# 14  Write a Python program to shuffle and print a specified list

# from random import shuffle
#
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# shuffle(color)
#
# print(color)

# 15  Write a Python program to generate and print a list of first and last 5 elements where the values
# are square of numbers between 1 and 30
#
# numbers = list(range(1, 31))
# first_five = numbers[1:6]
# last_five = numbers[25:]
# new_list = first_five + last_five
# new_list = [x*x for x in new_list]
# print(new_list)

# 16 Write a Python program to generate all permutations of a list in Python
# import itertools
# print(list(itertools.permutations([1,2,3])))

# 19. Write a Python program to get the difference between the two lists.
# print(list(set(range(1,5)) - set(range(1,3))))

# 20. Write a Python program access the index of a list.
# l = [1,2,3,4]
#
# for index, value in enumerate(l):
#     print(index, value)

# 21. Write a Python program to convert a list of characters into a string
# l = ['a', 'p', 'p', 'l', 'e']
#  print("".join(l))

# 22. Write a Python program to find the index of an item in a specified list.
# l = ["blue", "orange", "black", "yellow", "brown"]
# print(l.index("yellow"))

# 23. Write a Python program to flatten a shallow list.
# import itertools
# original_list = [[2,4,3], [1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)

#24 Write a Python program to append a list to the second list.
#
# list_one = list(range(1,4))
# list_two = list(range(4,11))
#
# list_one.append(list_two)
# print(list_one)

# 25. Write a Python program to select an item randomly from a list.

# import random
# l = [1,2,3,4]
# print(random.choice(l))

# 26 Write a python program to check whether two lists are circularly identical.
# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
#
# print('Compare list1 and list2')
# print(' '.join(map(str, list2)) in ' '.join(map(str,list1 *2)))
# print('Compare list1 and list3')
# print(' '.join(map(str,list3)) in ' '.join(map(str, list1 * 2)))

# 27. Write a Python program to find the second smallest number in a list.

# l = [200, 800, 600, 700]
# l.remove(min(l))
# print(min(l))

# 28. Write a Python program to find the second largest number in a list.

# l = [200, 800, 600, 700]
# l.remove(max(l))
# print(max(l))

# 29. Write a Python program to get unique values from a list
# l = [10,10,2,30,60,70,2,4,60,4,3]
# print(set(l))

# 30. Write a Python program to get the frequency of the elements in a list.
# l = [1,2,3,1,1,1,2,2,2,4]
# d = {i:l.count(i) for i in l}
# print(d)