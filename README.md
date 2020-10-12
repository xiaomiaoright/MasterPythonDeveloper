# Python Development
##Outline
1. Python Intro
2. Developer Environment
3. Object Oriented Programming
4. Functional Programming
5. Decorator
6. Error Handling
7. Generators
8. Modules in python
9. Debug
10. File I/O
11. Regular Expressions
12. Testing in Python
13.  Scripting data with pyhon
14. Scraping Data
15. Web development
16. Automation/Testing
17. Machine Learning

## 1. Python Intro
### 1.1 Python Data Types
[w3schools python data type reference](https://www.w3schools.com/python/python_datatypes.asp)

- Build-in data types
    - Text Type:	str
    - Numeric Types:	int, float, complex
    - Sequence Types:	list, tuple, range
    - Mapping Type:	dict
    - Set Types:	set, frozenset
    - Boolean Type:	bool
    - Binary Types:	bytes, bytearray, memoryview
- Customized data type
    - Class
### 1.2 Python Operators
[w3scholls python operators](https://www.w3schools.com/python/python_operators.asp)

- Python divides the operators in the following groups:
    - Arithmetic operators
    - Assignment operators
    - Comparison operators
    - Logical operators
    - Identity operators
    - Membership operators
    - Bitwise operators
- Operator Precedence
### 1.3 Python Math function
[math functions](https://docs.python.org/3/library/math.html)
### 1.4 Variables
[Python variable](https://www.w3schools.com/python/python_variables.asp)
### 1.5 Augmented assignment operator
[reference](https://docs.python.org/2.0/ref/augassign.html)
### 1.6 Type Conversion
```python
str(5)
```
### 1.7 Escape Sequences: \
- Whatever comes after "\" will be recgonized as a string. 
- "\t" means tab
- "\n" mean new line
```python
"It\'s \"kind  of\" a fruit"
# It's "kind of" a fruit

"\t Good morning!"
#   Good morning!
```
### 1.8 Format String

```python
name = "Tom"
age = 15
city = "Toronto"
print("{} is {} years old and is from city of {}".format(name, age, city))
print("{1} is {0} years old and is from city of {2}".format(age, name, city))
print(f"{name} is {age} years old and is from city of {city}") # f means formated string
```
### 1.9 String index: slicing
```python
city = "Toronto"
city[::-1] # reverse the string
```
### 1.10 Immutability
Immutability means cannot be changed.
A string can be reassigned, but cannot be changed by only one charater.

### 1.11 Build-in functions and Methods
- [Build-in functions](https://docs.python.org/3/library/functions.html)
- Methods: are functions owned by something, with brackets .methods()
    - [String methods](https://www.w3schools.com/python/python_ref_string.asp)
    ```python
    "my name is Tom".upper()
    ```
### 1.12 Colletection(array) data types: list, typle, set, dictionary
- There are four collection data types in the Python programming language:
    [Reference](w3schools.com/python/python_strings.asp)
    - List is a collection which is __ordered and changeable__. Allows duplicate members.
    - Tuple is a collection which is __ordered and unchangeable__. Allows duplicate members.
    - Set is a collection which is __unordered and unindexed__. No duplicate members.
    - Dictionary is a collection which is __unordered, changeable and indexed__. No duplicate members.

- Array: collection, one variable store many items
- Matrix: 2D array
- Dictionary
    - Key value pairs
        - Key needs to be immutable and unique (will be rewrite if duplicated), cannot be changed
    - [Reference](https://www.w3schools.com/python/python_dictionaries.asp)
- tuple
    - [reference](https://www.w3schools.com/python/python_tuples.asp)
    - ordered and unchangeable
- set
    - unordered and unindexed
    - unorded Collection of unique items
    - [Reference](https://www.w3schools.com/python/python_sets.asp)
    - Applications:
        - remove duplicates from list
        - difference from two sets
        - remove element from a set if a member
        - remove all elements of another set from this set
        - find common items between two set
        - confirm if two sets have items in common
        - union two sets
        - is subset or not
        - is superset or not
        ```python
        s_list = [1,2,3,4,5,2,4,3]
        s_set = set(s_list) # remove duplicates from list

        a_set = {1,2,3,4}
        b_set = {3,4,5,6}
        a_set.difference(b_set) # output: 1,2

        a_set.discard(5) # no element removed since 5 is not a member
        a_set.discard(4) # 4 is removed from a_set

        a_set.difference_update(b_set) # output is {1,2}. {3,4 }are elements of b_set so they are removed

        a_set.intersection(b_set) # 3,4

        a_set.isdisjoint(b_set) # False, they can join because commom items

        a_set.union(b_set) # {1,2,3,4,5,6}

        a_set.issubset(b_set) # false

        a_set.issuperset(b_set) # false

        ```

## Python Basics
### Flow and Logics
- Conditional Logic: if...elif...else
- Logical operators
- is vs. ==
- For Loops
- While Loops
- break, continue, pass
- range() and enumerate()

### developer fundmentals
- functions
- parameters and arguments
- default parameters and keywords
- return
- [Docstrings](https://www.datacamp.com/community/tutorials/docstrings-python)
- clean code
- *args and **kargs
    - take as many args kargs as needed
    ```python
    def getSum(*args, **kwargs):    
    return sum(args)+sum(kwargs.values())
    getSum(1,2,3,4,5, num1=5, num2=10)
    ```
- Rule: params, *args, default parameters, **kwargs
- Scope:
    - What variables do i have access to
        - local
        - parental
        - gloabl
        - build-in
    - global keyword

## Object Oriented Programming
[Object-oriented programming (OOP)](https://www.datacamp.com/community/tutorials/python-oop-tutorial?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9000839&gclid=EAIaIQobChMIsLbi46WJ7AIVA6_ICh2wbgLIEAAYASAAEgJkdPD_BwE) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). 

Defined with Class keyword.

### Object
- OOP uses the concept of objects and classes.

### Attributes and Methods
- Attributes
    - Class attributes, defined in __init__ method, dynamic
    - Class Object attributes, defined the same level as method, not dynamic
- __init__
- [@classmethod and @staticmethod](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)
```python
class NameOfClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def method(self):
        # method code
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        # classmethod code
        pass

    @ staticmethod
    def stc_method(param1, param2):
        # staticmethod code
        pass
```
### 4 pillars of OOP
- Encapsulation
- Abstraction
    - Private variable
    - Public variable
- Inhenritance
    - inheriant from parent class
- Polymorphism



### super()
inheriance parent class init

### introspection
```python
dir(wizard1)
```
### Dunder Methods
The methods defined with __ in name

issubclass()

### multiple inheritance
MRO: method resolution order
```python
className.mro()
```

## Functional Programming
### map()

### filter()

### zip()

### reduce()

### lambda expression

### list set dictionary comprehensions

## Python decorators
@classmethod
@staticmethod

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

Decorators are usually called before the definition of a function you want to decorate

## Error Handling
[Build in exceptions](https://docs.python.org/3/library/exceptions.html)

Good practice is always to catch errors based on specific exception


## Python Generators
```python
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
```

## Modules in Python
Module: each .py file is a module. Each module to build class/functions.

Package: is a folder containning modules. A package can have several modules.

Use import statement to import modules

### "__name\__"


### Build in modules
#### sys
```python
import sys
sys.argv

first = sys.argv[1]
last = sys.argv[2]

print(f'Hello {first} {last}')
```

```sh
$ python test.py Emily Lily
```

#### Your own package
- start with lower case letter: function
- start with capital letter: package


## Virtual Environments
```sh
$ pipenv
```

venv is an virtual environment created by python. Using venv to contain all the packages.


## Debug code
use of pdb package

## File I/O
### Input files
- Read txt file
```python
m_file = open(r'data\test.txt') # open file
m_file.read() # read all content
m_file.seek(0) # cursor back to the starting 
m_file.readlines() # read line by line
m_file.close() # close file
```

- with statement and mode
```python
# Use open statement
with open(r'data\test.txt', mode='r+') as my_file:
    text = my_file.write('Hey, it\'s me \n')
    print(text)
    print(my_file.readlines())
```

- create a translator
```python
# Translate file
from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open(r'data\trans_original.txt', mode='r') as trans_orig:
        text = trans_orig.read()
        translation = translator.translate(text)
        print(translation)
        with open(r'data\trans_tras.txt', mode = 'w') as trans_trans:
            trans_trans.write(translation)
except FileNotFoundError as err:
    print('file not found')
    raise err
```

## Python Regular Expression
[Reference](https://www.w3schools.com/python/python_regex.asp)

Tool: [ReGix101.com](https://regex101.com/)

- application of regular expression: email address check

- password check
```python
regex = r"[a-zA-Z0-9$%@#!]{8,}\d"
pattern = re.compile(regex)
test_str = "ding8fein5"
check = pattern.fullmatch(test_str)
check
```

## Testing
- Testing is important. 
- Use a test.py file together with other python files to be tested.
- style check package
    - pylint
    - pyflakes
    - PEP 8
- Built in module __unittest__
- [Reference](https://docs.python.org/3/library/unittest.html)