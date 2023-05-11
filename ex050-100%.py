# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
par = 0
for counter in range (1, 7):
    number = int(input('Enter the {}° number: '.format(counter)))
    if number % 2 == 0:
        soma += number
        par += 1
print('The sum of all {} Pair numbers are: {}'.format(par, soma))
