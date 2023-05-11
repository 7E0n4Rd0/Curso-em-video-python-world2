# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
#Example in Python:
'''a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for count in range (3,16):
    c = a + b
    print(c, end=' ')
    a = b
    b = c'''
print('{:=^40}'.format(' Fibonacci Sequence '))
n = int(input('How much terms of the Fibonacci Sequence do you want? '))
print('-=-'*20)
a = 0
b = 1
print('{} -> {} ->'.format(a, b),end=' ')
counter = 0
while counter < (n-2):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    counter += 1
    print('->' if counter != (n-2) else '', end=' ')
print('END')
print('-=-'*20)