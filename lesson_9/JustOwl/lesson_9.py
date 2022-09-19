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
from random import randint, random

class MyClass:
    def __init__(self, my_arg):
        self.my_arg = my_arg

class Animal():
    def __init__(self, arg1):
        self.my_arg = arg1

# Methods
"""
class Square():
    def __init__(self,size):
        self.size = size
    
    def area(self):
        return self.size*self.size 

    def circumference(self):
        return float(self.size) * 4

def main():
    square_one = Square(2)
    print(square_one.area())
    print(square_one.circumference())

    square_two = Square(3.5)
    print(square_two.area())
    print(square_two.circumference())


if __name__ == '__main__':
    main()
#Only print methods not a real instansiation
#print(f'A square with the sides of 2 has a Area of: {Square(2,2).area()}\nAnd a Circumference of: {Square(2,2).circumference()}' )
#print(f'A square with the sides of 3.5 has a Area of: {Square(3.5,3.5).area()}\nAnd a Circumference of: {Square(3.5,3.5).circumference()}')
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


def main():
    circle = Circle(2)
    print(circle.area())
    print(circle.circumference())
    print(circle.color)
    circle.set_color("red")
    print(circle.color)


if __name__ == '__main__':
    main()

#Same as above
#Circle.set_color(self=Circle,new_color="red") #Does not work and have no idea why
#circle_value = 3
#print(f'Area of the circle is: {Circle(circle_value).a}\nCircumference of the circle is: {Circle(circle_value).c}\nThe Color of the circle is: {Circle().color}')
"""
#EXTRA - Base class

class Person():
    def __init__(self,name,year):
        self.name = name
        self.year = year

class Player(Person):
    def __init__(self,name,year,stats):
        super().__init__(name,year)
        self.stats = stats

    def __str__(self):
        return f'{self.name}, {self.year}, {self.stats}'

class Coach(Person):
    def __init__(self,name,year,voice_level):
        super().__init__(name,year)
        self.voice_level = voice_level
    
    def __str__(self):
        return self.name

class Team():
    def __init__(self,player_ls,team_coach):
        self.player_ls = player_ls
        self.team_coach = team_coach
    
    def sum_team(self):
        team = ""
        team += f'Coach: {self.team_coach}\n'
        team += "Players:\n"
        team += "\n".join(map(str,self.player_ls))
        return team


def stat_gen():
    return (randint(1,10),randint(1,10),randint(1,10))

def main():
    coach = Coach("Göran",1969,7)
    players = []
    for name in ["lisa", "eva", "petra", "linda", "amanda", "jonna", "malin", "fredrika", "frida", "jenny"]:
        year = randint(1998,2003)
        players.append((Player(name,year,stat_gen())))
    
    team = Team(players,coach)
    print(team.sum_team())

if __name__ == '__main__':
    main()
