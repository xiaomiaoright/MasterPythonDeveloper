def my_decorator(func):
    def wrap_func(*args, **kwargs):
        # decoration code
        print('*'*10)
        func(*args, **kwargs)
        print('*'*10)
    return wrap_func

@my_decorator
def simple_func(mymessage):
    print(mymessage)


simple_func('I like Canada')

from time import time
def performance_decorator(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'running time: {t2 - t1} ms')
    return wrap_func

@performance_decorator
def comple_func(n):
    total = 0
    for x in range(n):
        total = total + x
    return total

comple_func(100000)