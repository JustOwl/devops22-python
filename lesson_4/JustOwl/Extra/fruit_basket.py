fruits = ["apple","orange","pear","banana","grapes"]

size = int(input("What is the size of you basket: "))

basket_ls = []


for i in range(size):
    if(i >= len(fruits)):
        i -= len(fruits)
    basket_ls.append(fruits[i])

print(basket_ls)