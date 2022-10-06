class User:
    def __init__(self, first_name:str, last_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name 

    def introduce_yourself(self):
        print(f'Hello! my name is {self.first_name} {self.last_name}')


Jonathan = User("Jonathan", "Moore")

# print(Jonathan.first_name)

# Jonathan.introduce_yourself()


class Athlete:
    def __init__(self, name:str, sport:str, age:int) -> None:
        self.name = name
        self.sport = sport
        self.age = age
        self.injured = False
    
    def __repr__(self) -> str:
        attributes = vars(self) #this returns a dictionary of the keys and what values they represent
        for key, value in attributes.items():
            print(f'Attribute "{key}" is set to "{value}"!')
        # print(attributes)
        return f'Hello! This is the {self.name} object!'

    def injure_player(self):
        self.injured = True
        print(f'{self.name} is injured! On No!')


tom_brady = Athlete('Tom Brady', 'football', 45)

print(tom_brady)
# print(tom_brady.injured)

# tom_brady.injure_player()

# print(tom_brady.injured)