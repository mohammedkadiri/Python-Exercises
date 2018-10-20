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