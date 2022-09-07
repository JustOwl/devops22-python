import string


firstname = "john"
lastname = "smith"
tele = "00468123456789"

fullname = (f'{firstname} {lastname}')

print(fullname[:5])

print(fullname[1:-1])

odd_chars = ""
even_chars = ""

for i in range(len(fullname)):
    if i%2 == 0:
      even_chars = even_chars + fullname[i]
    else:
        odd_chars = odd_chars + fullname[i]
        

print(f'Even characters: {even_chars}, Odd characters: {odd_chars}')

print(fullname[::-1])


#print(fullname[5])