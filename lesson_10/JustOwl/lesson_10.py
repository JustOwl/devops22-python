#override
"""
class Myclass():
    def my_method():
        return f'My base method'

class SecondClass(Myclass):
    def my_method():
        return f'My second method'

a = Myclass()
b = SecondClass()

print(a.my_method)
print(b.my_method)
"""
#menu
"""

class Dog():
    def __init__(self):
        self.v = "I am a dog"
    

class Menu():
    
    def __init__(self):
        self.run = False
        self.new_obj = ""
        self.menu_commands = {1: self.Creat_obj,
                              2: self.Print_obj,
                              3: self.Destroy_obj}

    def Creat_obj(self):
        self.new_obj = Dog()
        return self.new_obj

    def Print_obj(self):
        try:
            if(self.new_obj == ""):
                print("No object to print")
            else:
                print(str(self.new_obj))    
        except Exception:
            print("Sorry something went wrong")
            self.run == False
    def Destroy_obj(self):
        try:
            if(self.new_obj == ""):
                print("No object to delete")
            else:
                del(self.new_obj)
        except Exception:
            print("Sorry something went wrong")
            self.run == False

    def start_loop(self):
        self.run = True
        while self.run:
            print(f'Menu\n1:Creat \n2:Print \n3:Destroy')  
            choice = int(input("Enter input [1-3]:"))
            self.menu_commands[choice]()

def main():
    Menu().start_loop()

if __name__ == '__main__':
    main()
"""
#Composition vs Inheritance

class Person():
    def __init__(self, adress, street_name,street_num,postal,country):
        self.adress = adress
        self.street_name = street_name
        self.street_num = street_num
        self.postal = postal
        self.country = country

        self.info = (self.adress,self.street_name,self.street_num,self.postal,self.country)
        

