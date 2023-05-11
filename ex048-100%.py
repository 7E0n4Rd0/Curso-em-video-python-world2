# Exercício 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
c = 0
for counter in range(1, 501):
    if counter % 2 == 1 and counter % 3 == 0:
        s += counter
        c += 1
print('The sum of the {} numbers multiple by 3 and Impar in the range for 1 to 500 is {}'.format(c ,s))
