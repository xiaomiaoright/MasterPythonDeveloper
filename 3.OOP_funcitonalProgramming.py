# map function
from functools import reduce
def simple_calculator(num):
    return num**2
li = [1,2,3]
li_squ = list(map(simple_calculator, li))
li_squ

list(map(lambda x: x**2, [1,2,3]))

# zip function
li_1 = [x for x in 'abcd']
li_2 = [x for x in range(4)]
list(zip(li_1, li_2))

# filter function
li = [x for x in range(100)]
list(filter(lambda x: x%5==0, li))


# reduce function
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
from functools import reduce
li = [x for x in range(5)]
def simple_sum(acc, num):
    return acc+num
reduce(simple_sum, li, 0)


reduce((lambda x, y: x * y), [1, 2, 3, 4], 10)

