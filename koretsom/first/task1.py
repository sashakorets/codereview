'''
знайти суму чисел із едементів списку
'''

data = ['dasdasd',2,'dsadasda',23]
suma1 = 0
for number in data:
    if type(number) == float or type(number) == int :
        suma1 = suma1 + number
    else:
        continue
print(suma1)