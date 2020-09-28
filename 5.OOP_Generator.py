# range() is generator
from time import time
range(0,100) # create a number one by one
list(range(0,100)) # create a list use memory to store 100 numbers together

# list is an iterable, with __inter__ method

# create a generator with key word yeild

def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(100):
    print(item)

g = generator_function(100)
next(g)
iter(g)
next(iter([1,2,3]))


# compare performance of list(range(100)) and range(100)
def performance_decorator(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'running time: {t2 - t1} ms')
    return wrap_func

@performance_decorator
def long_time1():
    print("1")
    for i in list(range(10000000)):
        i*5


@performance_decorator
def long_time2():
    print("2")
    for i in range(10000000):
        i*5

long_time1()
long_time2()


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3,4,5])

class myGen():
    current = 0
    def __init__(self, first, last):
        self.start = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if myGen.current < self.last:
            num = myGen.current
            myGen.current += 1
            return num
        raise StopIteration

gen = myGen(0, 10)
for i in gen:
    print(i)


# Fibonacci Numbers with Generator
def fib(indexNum):
    a = 0
    b = 1
    for i in range(indexNum):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(10):
    print(x)

class FibGenerator():
    i = 0
    a = 0 
    b = 1
    
    def __init__(self, indexNum):
        self.end = indexNum

    def __iter__(self):
        return self

    def __next__(self):
        if FibGenerator.i < self.end:
            if FibGenerator.i == 0:
                FibGenerator.i += 1
                return FibGenerator.a

            else:
                temp = FibGenerator.a
                FibGenerator.a = FibGenerator.b
                FibGenerator.b = temp + FibGenerator.b
                FibGenerator.i += 1
                return FibGenerator.a
        raise StopIteration

fibGen = FibGenerator(10)
for i in fibGen:
    print(i)
