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
class MyClass:
    def __init__(self, my_arg):
        self.my_arg = my_arg

class Animal():
    def __init__(self, arg1):
        self.my_arg = arg1

class Square():
    def __init__(self,my_arg):
        self.my_arg = my_arg
    
    def square_math(self):
        return self.my_arg * 2

sq = Square()

print(sq(2).square_math)
