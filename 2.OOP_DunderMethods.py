class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": 'Yoyo',
            "has_pets": False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yes??'

    def __getitem__(self, i):
        return self.my_dict[i]

myToy = Toy('red', 0)
myToy.__str__()
myToy.__len__()
myToy()
myToy['name']