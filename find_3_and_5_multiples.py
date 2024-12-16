from functools import reduce

def find_multiples(num):
    three_numbers = list(range(0, num, 3))[1:]
    five_numbers = list(range(0, num, 5))[1:]
    all_num_without_duplicates = list(set(three_numbers + five_numbers))
    return reduce(lambda x,y: x + y, all_num_without_duplicates)


print(find_multiples(10))
print(find_multiples(600))

