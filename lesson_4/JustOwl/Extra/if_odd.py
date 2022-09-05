int_ls = [2,4,6,8,10,11]

for item in range(len(int_ls)):
    if(int_ls[item]%2 == 0):
        continue
    else:
        print(f'{int_ls[item]} is not allowed!')
        break