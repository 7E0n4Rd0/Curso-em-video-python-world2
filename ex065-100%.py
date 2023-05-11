#Exercício 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lidos. O programa deve perguntar ao usuário se ele quer continuar a digitar valores.
bigger = lower = 0
answer = str('Y')
while answer == 'Y':
	numbers = int(input('How much numbers do you need? '))
	print('-=-'*20)
	counter = s = 0
	while counter < numbers:
		n = int(input('Enter {}° number: '.format(counter+1)))
		if counter == 0:
			bigger = n
			lower = n
		s += n
		counter += 1
		if n > bigger:
			bigger = n
		elif n < lower:
			lower = n
	media = s/numbers
	print('~'*60)
	print('The Media is {:.2f}, The Bigger Number is {}, The lower Number is {}'.format(media, bigger, lower))
	print('~'*60)
	answer = str(input('Do you want to continue? [Y/N] ')).strip()[0].upper()
print('END')
# A maior parte do programa já fiz durante a festa, vou descansar e deixar para amanhã ou um próximo dia. 04/22/2023 - 21:47
# Pronto, acabei de arrumar o código •-•. 04/22/2023 - 21:50
# This commentary is in English reader: I'm watching the correction of the exercise, my code is kinda different because his propose was for every number typed by keyboard has a questions "Do you want to continue?" and my code ask "how much number do you need" then It has the question "Do you want to continue?". I think it's good what I did, mostly I maded in a party Lol. - 04/23/2023 - 20:59