
# 1. Write a Python program to read an entire text file

# with open('file1.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)


# 2. Write a Python program to read first n lines of a file
# with open('file1.txt', 'r') as f:
#     n = 10
#     f_contents = f.read(n)
#     print(f_contents)

# 3. Write a Python program to append text to a file and display the text.

# with open('file1.txt', 'a') as f:
#     f.write(' can i also append text')
#
# f1 = open('file1.txt', 'r')
# f_contents = f1.read()
# print(f_contents)
# f1.close()


# 5. Write a Python program to read a file line by line and store it into a list
# with open('file2', 'r') as f:
#     f_contents = f.readlines()
#     print(f_contents)
#
# s = "".join(f_contents)
#
# s = s.replace("\n", " ")
#
# s = s.split()
# print(s)

# 6 Write a python program to find the longest words.
#
# def longest_word(filename):
#     with open(filename, 'r') as f:
#         words = f.read().split()
#     max_length = len(max(words, key=len))
#     return  [word for word in words if len(word) == max_length]
#
# print(longest_word('file3'))
