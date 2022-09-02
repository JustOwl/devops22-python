from os import times_result


time = input("Input Seconds:")

minutes = int(time)//60
hours = int(time)//3600
days = int(time)//86400

print(f'Days:{days}, Hours:{hours}, Minutes:{minutes}')