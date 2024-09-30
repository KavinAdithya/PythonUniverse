a : int = int(input('Enter the first Number : '))
b : int = int(input('Enter the Second Number : '))

temp = b
b = a
a = temp

print(b ,'is swapped as ', a, 'and', a, 'is swapped as', b)