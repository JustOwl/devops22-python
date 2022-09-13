def print_num(start = 1, stop= 11):
    for i in range(start,stop):
        print(i)

def print_string(string,reverse = False):
    if reverse == True:
        print(string[::-1])
    else:
        print(string)

print_num()
print_string("hello")
print_string("hello",True)
