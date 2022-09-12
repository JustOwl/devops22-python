from random import Random, random, randrange
import random

num_ls = []
even_ls = []
odd_ls = []
random_100_set = {None}
color_ls = ["green","blue","orange","yellow","grey"]
red_color_ls =["red"]
for i in range(100):
    num_ls.append(i+1)

for i in range(2,61):
    if i%2 == 0:
        even_ls.append(i)

for i in range(1,78):
    if i%2 == 1:
        odd_ls.append(i)

while len(random_100_set) < 100:
    random_100_set.add(randrange(1,300))

red_color_ls.append(random.choice(color_ls))
red_color_ls.append(random.choice(color_ls))
new_color_ls = []
for i in range(50):
    new_color_ls.append(random.choice(red_color_ls))

print(f'Color_ls len: {len(color_ls)}, Red_color_ls len: {len(red_color_ls)}, New_color_ls len: {len(new_color_ls)}')
color_set = set(color_ls)
red_color_set = set(red_color_ls)
new_color_set = set(new_color_ls)

print(color_set)
print(red_color_set)
print(new_color_set)