x = True
y = True
z = True

if(x or y or z):
    print("Any are True")

if(x and y and z):
    print("All are True")

if((x and y and z) != True):
    print("Any is False")

if((z and y and z) == True):
   print("Any is True")

