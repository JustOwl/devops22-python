import math 
person_1 = "Alpha" #input("Enter name for person 1: ")
age_1 = 1 #input(f'Enter age for {person_1.title()}: ')
shoe_1 = 12 #input(f'Enter shoe size for {person_1.title()}: ')


person_2 = "Beta" #input("Enter name for person 2: ")
age_2 = 2 #input(f'Enter age for {person_2.title()}: ')
shoe_2 = 22 #input(f'Enter shoe size for {person_2.title()} : ')

person_3 = "Delta"#input("Enter name for person 3: ")
age_3 = 3 #input(f'Enter age for {person_3.title()}: ')
shoe_3 = 33#input(f'Enter shoe size for {person_3.title()} : ')

print(f'{person_1.title()} is {age_1} years old and has a shoe size of {shoe_1}')
print(f'{person_2.title()} is {age_2} years old and has a shoe size of {shoe_2}')
print(f'{person_3.title()} is {age_3} years old and has a shoe size of {shoe_3}')
"""
person_ls = [person_1, person_2, person_3]
age_ls = [age_1,age_2,age_3]
"""
shoe_ls = [shoe_1,shoe_2,shoe_3]
age_dict = {person_1:age_1,
            person_2:age_2,
            person_3:age_3}

oldest_person = sorted(age_dict, key=lambda age_dict: age_dict[0], reverse=True)
print(f'The oldest person is {oldest_person[0]} and has a shoe size of {age_dict[oldest_person[0]]}')

"""
for item in range(len(person_ls)):
    if(oldest_person[0] == person_ls[item]):
        print(f'The oldest person is {oldest_person[item]} and has a shoe size of {}')
"""
shoe_dict = {shoe_2}



shoe_ls.sort()
middle_shoe = (len(shoe_ls)-1)//2
print(f'The person with median shoe size is {None}')