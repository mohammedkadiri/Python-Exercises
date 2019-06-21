
# Taking a arbitrary number of marks single asterik use tuple
# def student(name, age, *marks):
#     print(name)
#     print(age)
#     print(marks)
#
# student('jake', 19, 90,80,70,60)


# Taking a arbitrary number of marks double asterik can use dict

def student(name, age, **marks):
    print(name)
    print(age)
    for key, value in marks.items():
        print(key, '', value)

student('joe', 20,  english=90, math=80, history=78)