# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
primo = int(0)
number = int(input('Enter some number: '))
for counter in range(1,number+1):
    if number % counter != 0:
        print('\033[31m{}\033[m'.format(counter), end=' ')
    elif number % 1 == 0 and number % number == 0:
        print('\033[32m{}\033[m'.format(counter), end=' ')
        primo += 1
print('\nCounter of the number of divisions:',primo)
if primo == 2:
    print('This number: {} is PRIME.'.format(number))
else:
    print('This number: {} is not PRIME.'.format(number))