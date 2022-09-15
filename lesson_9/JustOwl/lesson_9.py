#Classes
"""
class Animal():
    pass

class Dog(Animal):
    pass

class Supermarket():
    pass

class Coop():
    pass
"""
#__init__
from cmath import pi


class MyClass:
    def __init__(self, my_arg):
        self.my_arg = my_arg

class Animal():
    def __init__(self, arg1):
        self.my_arg = arg1

# Methods
"""
class Square():
    def __init__(self,w,h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h 

    def circumference(self):
        return float(self.w) * 4

print(f'A square with the sides of 2 has a Area of: {Square(2,2).area()}\nAnd a Circumference of: {Square(2,2).circumference()}' )
print(f'A square with the sides of 3.5 has a Area of: {Square(3.5,3.5).area()}\nAnd a Circumference of: {Square(3.5,3.5).circumference()}')
"""
# Circle
"""
class Circle():
    def __init__(self, diagonal = 1, color = "grey"):
        self.diagonal = diagonal
        self.color = color
        self.a = Circle.area(self)
        self.c = Circle.circumference(self)
    
    def area(self):
        return ((self.diagonal/2)**2)*pi
    
    def circumference(self):
        return self.diagonal*pi
    
    def set_color(self,new_color):
        self.color = new_color

Circle.set_color(self=Circle,new_color="red") #Does not work and have no idea why
circle_value = 3
print(f'Area of the circle is: {Circle(circle_value).a}\nCircumference of the circle is: {Circle(circle_value).c}\nThe Color of the circle is: {Circle().color}')
"""
#EXTRA - Base class

class Person():
    def __init__(self,name,year):
        self.name = name
        self.year = year

class Player(Person):
    def __init__(self,speed,agility,strength):
        self.speed = speed
        self.agility = agility
        self.strength = strength

        return speed(range(1,10)),agility(range(1,10)),strength(range(1,10))

class Coach(Person):
    def __init__(self,voice_level):
        self.voice_level = voice_level
        return voice_level(range(1,10))

class Team():
    def __init__(self,player_ls,team_coach):
        self.player_ls = player_ls
        self.team_coach = team_coach
    
    def sum_team(self):
        print(f'Team list: {self.player_ls}\nCoach: {self.team_coach}')

#TODO Input players(name, age)* amount of players,
