# Printing a set
setx = set()
print(setx)
x = 0
# Iteration over sets
num_set = set([1,2,3,4])
for x in num_set:
    print(x)
# Add members in set
color_set = set()
color_set.add("Yellow")
print(color_set)
#Add multiple items to a set
color_set.update(["Blue","Green"])
print(color_set)
#Remove,pop,discard functions to remove individual item from a set
num_set = set([0,1,2,3,4])
num_set.pop()
print(num_set)
#remove an element in the set
num_set = set([0,1,2,3,4])
num_set.remove(0)
print(num_set)
#discard an element in the set
num_set = set([0,1,2,3,4])
num_set.discard(3)
print(num_set)