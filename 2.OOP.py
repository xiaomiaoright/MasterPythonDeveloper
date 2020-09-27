class PlayerCharacter:
    membership = True # class object attribute
    def __init__(self, name, age):
        if self.membership and (age > 18):
            self.name = name # class attribute
            self.age = age
    
    def run(self):
        print('RUN!')
        return 'Done!'
    
    def shout(self):
        print(f'my name is {self.name}. I am {self.age} years old.')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def adding_Object(cls,name, num1, num2):
        print(cls.membership)
        return cls(name, num1 + num2)
    # classmethod, related to the class state by using the cls parameter such class attribute.

    @staticmethod
    def adding2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Tom", 30)
# player1.run()

# player1.name
player1.shout()
player1.adding_things(2,3)
PlayerCharacter.adding_things(2,3)
player2 = PlayerCharacter.adding_Object("Teddy", 12, 13)
player2.age
PlayerCharacter.adding2(3,19)
# player1.membershipStatus()
