user_name = "Kalle"
salary = 10000
flag = False

print(f'{user_name} your current salary is {salary}')

new_salary = input("How much would you like to increase it by?")
print(f'Haha \N{face with tears of joy} No')

while True:
    new_salary = input("How much would you like to increase it by?")

    if((int(new_salary)/int(salary)) > 0.05):
        print("No thats too much")
    else:
        flag = True
        break

if(flag):
    print("Ok that looks good")
    salary += int(new_salary)
    print(f'This is your new salary: {salary}')

if(flag == False):
    print("Im sorry but your offers were too high")
