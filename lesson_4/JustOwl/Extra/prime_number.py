prime_ls =[]
non_prime_ls = []
n = 1

while n <= 100:
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if(n % i) == 0:
                break
            else:
                prime_ls.append(n)
    n += 1


def is_prime(number):
    if number > 1:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                return False
        return True
    return False
"""
for i in range(0,100):
    if(is_prime(i)):
        prime_ls.append(i)
"""
print(set(prime_ls))