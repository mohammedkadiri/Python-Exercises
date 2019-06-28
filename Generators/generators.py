
def square_numbers(nums):
    for i in nums:
        yield(i * i)


val = [i for i in range(2, 11) if i % 2 == 0]

my_nums = square_numbers(val)

for num in my_nums:
    print(num)




