from colorama import Fore, Back, init

init(convert=True)

print(Back.GREEN)
print(Fore.BLACK)

operation = input('+ или -: ')

a = float(input('первое число '))
b = float(input('второе число '))

if operation == '+':
    print('result: ', str(a+b))
elif operation == '-':
    print('result: ', str(a-b))
else:
    print(Back.RED)
    print('WRONG OPERATION')

input('')