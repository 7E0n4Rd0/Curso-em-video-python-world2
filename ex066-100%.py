# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre elas (desconsiderando o flag).
n = c = s = 0
while True:
    n = int(input('Enter some number (Press 999 to stop): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'The sum of {c} numbers typed is {s}.')
