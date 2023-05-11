# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 
# 3 para hexadecimal.
# I don't know how to do this because I don't have knowlegde about "Base numérica". So I'll skip this and watch the
# video corecting this exercise. - 03/11/2023 - 18:43
number = int(input('Enter some int number: '))
print('''Choose one of the convertions bases:
[1] Convert to BINARE
[2] Convert to OCTAL
[3] Convert to HEXADECIMAL''')
option = int(input('Enter your option: '))
# if option == 1:
#   print('{} converted to BINARE is {}'.format(number, bin(number)[2:]))
# elif option == 2:
#   print('{} converted to OCTAL is {}'.format(number, oct(number)[2:]))
# elif option == 3:
#   print('{} converted to HEXADECIMAL is {}'.format(number, hex(number)[2:]))

if option == 1:
    print('{} converted to BINARE is {:b}'.format(number, number))
elif option == 2:
    print('{} converted to OCTAL is {:o}'.format(number, number))
elif option == 3:
    print('{} converted to HEXADECIMAL is {:x}'.format(number, number))
else:
    print('It does not exist this option!')
# No funcking way, this shit was easy 💀. It was just to put "bin()","oct()" and "hex()". - 03/11/2023 - 19:03
# An alternative way to convert is puting {:b} -> BINARE, {:o} -> OCTAL, {:x} or {:X} -> HEXADECIMAL/Lower,Upper
