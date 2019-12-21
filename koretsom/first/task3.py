'''
знайти середнє значення цілих чисел в діапазоні заданому користувачем
'''

a=float(input('first number'))
b=float(input('second number'))
second_var=0
i=0
for number in range(int(min(a,b)),int(max(a,b))+1):
    second_var=second_var+number
    i+=1
print(second_var/i)