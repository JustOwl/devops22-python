first_ls = [2,4,6,8,10]
second_ls = [10,8,6,4,2]
new_tuple = ()
new_ls = []

for i in range(len(first_ls)):
    i_first_ls = first_ls.index(second_ls[i])
    new_tuple = (second_ls[i],i_first_ls)
    new_ls.append(new_tuple)

print(new_ls)