def user_input():
    return input("Please input two numbers and an operator(+,-,*,/,%): \n Input format: first number,secondnumber,operator:").split(",")

def lambda_calc(x,y,operator):
    lambda_dict = {"+":lambda x: x+y,
                   "-":lambda x: x-y,
                   "*":lambda x: x*y,
                   "/":lambda x: x/y,
                   "%":lambda x: x%y}
    return lambda_dict[operator]

a,b,c = user_input()

test = lambda_calc(a,b,c)
print(int(test))

