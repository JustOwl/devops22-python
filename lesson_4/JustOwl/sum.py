start_int = input("Input starting number:")
end_int = input("Input ending number:")

current_int = int(start_int)
sum_int = 0

while(current_int <= int(end_int)):
    print(current_int)
    sum_int += current_int
    current_int+=1

print("Sum: ",sum_int)

