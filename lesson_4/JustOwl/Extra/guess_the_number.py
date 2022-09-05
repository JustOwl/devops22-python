my_number = 42

user_number = int(input("Guess my number: "))

if(user_number == my_number):
        print("Correct! that is my number, how did you know on the first try?")

while user_number != my_number:
    if(user_number < my_number):
        print("Wrong, it's higher")
        user_number = int(input("Enter a new number: "))
    if(user_number > my_number):
        print("Wrong, my number is lower")
        user_number = int(input("Enter a new number: "))
    if(user_number == my_number):
        print("Correct! that is my number")
        break
