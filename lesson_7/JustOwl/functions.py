def do_nothing():
    pass

def hello_world():
    print("hello world")

def one_equals_one():
    print(1 == 1.0)

def reverse_ls(ls):
    print(sorted(ls,reverse=True))

def hello_name(name):
    print(f'Hello {name}')

def capital_word(word):
    print(word.capitalize())

def print_until(stop):
    for i in range(1,stop):
        print(i)

aplhabet_ls = ["a","b","c","d","e"]

hello_world()
one_equals_one()
reverse_ls(aplhabet_ls)
hello_name("Kalle")
capital_word("wOrDs")
print_until(6)