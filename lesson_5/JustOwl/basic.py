firstname = "john"
lastname = "smith"
tele = "00468123456789"

fullname = (f'{firstname} {lastname}')

print(firstname,lastname,tele)
print(fullname)

print(len(fullname),len(firstname),len(lastname))

print(f'{fullname}\n{tele}')

print(fullname+tele)
print(f'{fullname},{tele}')
print('{}'.format(fullname+tele))
print('A name %s' %fullname+tele)