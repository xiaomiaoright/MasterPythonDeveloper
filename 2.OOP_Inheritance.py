class User():
    def sign_in(self):
        print("logged in")
    
    def attack(self):
        print("Nothing happened")

class Wizard(User):
    # inherate from parent class User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self) # call parental class methods
        print(f'Attack with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'Attack with arrow. Number of arrows left: {self.arrow}')

wizard1 = Wizard('Emily', 50)
archer1 = Archer('Time', 20)
wizard1.sign_in()
wizard1.attack()
archer1.attack()

# Check if a instantce is from a class (object)
isinstance(wizard1,Wizard)
isinstance(wizard1, User)
isinstance(wizard1, object)
