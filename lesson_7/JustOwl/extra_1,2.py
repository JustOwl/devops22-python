def more_than_five(x):
    print(x*int(x))

def less_than_five(num):
    for i in range(1,int(num)+1):
        print(i*str(i))

num = input("Enter number:")

if int(num) <= 5:
    less_than_five(num)
else:
    more_than_five(num)
     