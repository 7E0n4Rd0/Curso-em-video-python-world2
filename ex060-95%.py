# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
number = int(input('Enter some number: '))
counter = number
print('{}! = '.format(number),end='')
while counter != 0:
    print('{}'.format(counter), end='')
    counter -= 1
    # if counter != 0:
    #     print(' x ',end='')
    # elif counter == 0:
    # Optimizing the if
    print(' x ' if counter > 0 else ' = ', end= '')
print('{}'.format(factorial(number)), end='')
