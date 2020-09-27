class User():
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print("logged in")
    
    def attack(self):
        print("Nothing happened")

class Wizard(User):
    # inherate from parent class User
    def __init__(self, name, power, email):
        super().__init__(email)
        # or use: User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self) # call parental class methods
        print(f'Attack with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrow, email):
        super().__init__(email)
        # User.__init__(self, email)
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'Attack with arrow. Number of arrows left: {self.arrow}')

wizard1 = Wizard('Emily', 50, "emily@gmail.com")
archer1 = Archer('Time', 20, 'time@gmail.com')
wizard1.sign_in()
wizard1.email

wizard1.attack()
archer1.attack()

# Check if a instantce is from a class (object)
isinstance(wizard1,Wizard)
isinstance(wizard1, User)
isinstance(wizard1, object)


# introspection
dir(wizard1)


class superDict(dict):
    def __len__(self):
        return 5

    def add_item(self, newKey, newValue):
        self[newKey] = newValue


a = {"a": 1}
len(a)
a['b'] = 2
a

a = superDict()
a.add_item('a', 1)
a



# multi inheritance
class Hybird(Wizard, Archer):
    def __init__(self, name, power, arrow, email):
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrow, email)

hy1 = Hybird('Emily', 20, 15, 'emily@gmail.com')
hy1.attack()
hy1.sign_in()


# Method Resolution Orders
class A():
    num = 10

class B(A):
    pass

class C(A):
    num = 20

class D(B, C):
    pass

D.mro()
D.num