vip_ls = ("Alpha", "Beta","Charlie", "Delta", "Foxtrot")

name = input("Please input your name:")

if(any(name in value for value in vip_ls)):
    print(f'Welcome {name} you are on the list')
else:
    print(f'Sorry {name} you are not on the list')