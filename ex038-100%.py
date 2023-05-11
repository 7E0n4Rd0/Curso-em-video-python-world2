# Exercício Python 038: escreva um programa que leia dois números inteiros e compare-os. Mostrando uma mensagem na tela:
# — O primeiro valor é maior
# — O segundo valor é maior
# — Não existe valor maior, os dois são iguais.
number01 = int(input('Enter the first number: '))
number02 = int(input('Enter the second number: '))
if number01 > number02:
    print('The first number: {} is bigger than the second number: {}'.format(number01, number02))
elif number02 > number01:
    print('The second number: {} is bigger than the first number: {}'.format(number02, number01))
else:
    print('The are the same number: {}'.format(number01))
