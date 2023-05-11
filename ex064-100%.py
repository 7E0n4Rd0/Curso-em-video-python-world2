# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
s = 0
counter = 0
# n = s = counter = 0
while n != 999:
	n = int(input('Enter some number [Press 999 to stop]: '))
	if n != 999:
		counter += 1
		s += n
	else:
		counter += 0
		s += 0
print('Counter {}, Sum {}'.format(counter, s))