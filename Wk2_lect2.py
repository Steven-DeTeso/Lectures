# Office hours, More of the "Basic 13" algorithim challenges. Always going to put inside function. 

# starting where we left off from last week 

# 4) Array with Odds - create an array with all the odd integers between 1 and 255 (inclusive).
def array_of_odds():
    odd_list = []
    for i in range(1, 256):
        if i % 2 == 1: 
            odd_list.append(i)
    return odd_list

# print(array_of_odds())

"""
Lecture starts here: 
Lecture is still all about OOP, Jonathan opens with the usual housekeeping stuff. 
Git is SUPER important in Projects and Algorithims week, so learn it now! 

What is the difference between an object and a dictionary?
    Dictionaries are just data structures that data can go inside of.
        dictionaries can just be made 
    Objects are instances of a class. 
        objects have to be copies of a class. 

What are some examples of when to use a class. 
    Recipes, character customazation, social media profiles, car class, (anyting that requires parts, like making a pizza)
"""
"""
Today we are coving OOP! 
    Class association 
    Database example
    @classmethods and @static methods
    Four Pillars
"""

# Class association - you define an attribute of one class by referring to another class. Need to have multiple classes and tie them together by having them reference each other. 

class User:
    def __init__(self, f_name:str, l_name:str, age:int):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.pets = []

    
    def __repr__(self) -> str: # for our output terminal
        return f'This is the {self.first_name} {self.last_name} object'

class Pet:
    def __init__(self, name:str, species:str, breed:str, adorableness:int = 10):
        self.name = name
        self.species = species
        self.breed = breed
        self.adorableness = adorableness
        self.owner = None # this None gets filled in later by moose.owner = instance jonathan

    def __repr__(self) -> str:
        return f'This is the {self.species} object'

jonathan = User('Jonathan', 'Moore', 26)

moose = Pet(species = 'dog', name = 'Moose', breed = 'black lab') #order doesn't matter while defining the instance of the Pet class here because key value's are specified. 
tigger = Pet(species = 'cat', name = 'Tigger', breed = 'short hair')

moose.owner = jonathan #type: ignore

jonathan.pets.append(moose)
jonathan.pets.append(tigger)

print(moose.owner) # by calling the moose.owner you have access to the jonathan object. This associates the pet class with the user class through this 'bridge'

print(jonathan.pets)

# What we did above, is create a relationship or assocition between the User and Pet classes. 