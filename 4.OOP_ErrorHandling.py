age = int(input("what is your age? "))

while True:
    try:
        age = int(input("what is your age? "))
        100/age
        print(age)
        raise ValueError('Hey, cut it out')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter number larger than 0')
    else: 
        print('thank you')
        break
    finally:
        print('it is finally done')

def simple_sum(n1, n2):
        try:
            return n1+n2
        except TypeError as err:
            print(f'please enter a number. {err}')
        else:
            'thank you'
        finally:
            print('it is finally done')
simple_sum(1, '1')

print(TypeError)