def user_input():
    return input("Please input two numbers and an operator(+  - * / %): \n Input format: first number,secondnumber,operator:").split(",")

def lambda_calc(operator):
    lambda_dict = {"+":lambda x,y: x+y,
                   "-":lambda x,y: x-y,
                   "*":lambda x,y: x*y,
                   "/":lambda x,y: x/y,
                   "%":lambda x,y: x%y}
    return lambda_dict[operator]

a,b,c = user_input()

test = lambda_calc(c)
print(test(float(a),float(b)))