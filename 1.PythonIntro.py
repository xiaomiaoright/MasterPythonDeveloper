# binary function
bin(5)
int('0b101',2)

import math
math.pi

name = "Tom"
age = 15
city = "Toronto"
print("{} is {} years old and is from city of {}".format(name, age, city))
print(f"{name} is {age} years old and is from city of {city}")
city[::-1]

any([])

type(False)

name = input("Please input your name: ")
password = input("What is your password? ")
pw = len(password)
pws = "*" * pw
print(f"{name}, your password {pws} is {pw} letters long")

m = [
    [1,2,3],
    [11,22,33]
    ]
len(m)
import numpy as np
m_arr = np.array(m)
m_arr.shape

m.append([1,2])
m.append(1)
m
m +[1,2,3]
m.insert(0, 'start')
m
np.array(m).shape
m.pop()
m.pop(0)
m.remove([1,2])
m.clear()
m.extend([1,2,3])
m
m+[1,2,3]
m.index(1)
m.append('start')
m
'start' in m
m.count(1)
m.sort()
sorted([1,5,2,8,3])[::-1]
print([1,5,2,8,3].sort())
m = [1,5,2,8,3]
n = m.copy()
n.sort()
n
m
n.reverse()
n

d= {'a': 1, 'b':2}
d
d['a']
d.values()
d.keys()
'a' in d.keys()
1 in d.values()

d.clear()
d.pop('a')
d.popitem()
d['a'] = 2
d['a']

s = {1,2,3,4,5}
s.add(6)
set([1,2,3,4,4,6,3,7,1,2]) # remove duplicates


n = [1,2,3,4,4,6,3,7,1,2]

n.count(1)

def string_reverse(inputString): 
    '''
    Info: this function reverse the inputString and return it
    '''
    return inputString[::-1]

string_reverse("Like")
print(string_reverse.__doc__)
help(string_reverse)

def getSum(*args, **kwargs):
    
    return sum(args)+sum(kwargs.values())
getSum(1,2,3,4,5, num1=5, num2=10)

def highest_even(li):
    li_even = [x for x in li if x % 2 == 0]
    return sorted(li_even)[-1]

highest_even([2,1,4,6,3,4,844,1])