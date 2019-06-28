

def count_down(n):
    i = n

    while i >= 0:
        yield i
        i -= 1

for x in count_down(5):
    print(x)


