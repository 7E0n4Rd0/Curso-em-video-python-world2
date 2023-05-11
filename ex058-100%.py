# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
import random
print('{:=^40}'.format(' Guesing Game '))
sleep(3)
print('I am thinking in a number...')
sleep(3)
computer = random.randint(0, 10)
print(computer)
player = int(input('Which number I thought? '))
player_counter = int(1)
while player != computer:
    if computer < player:
        player = int(input('The number is\033[1;33m Lower\033[m. Try Again: '))
        player_counter += 1
    elif computer > player:
        player = int(input('The number is\033[1;31m Higher\033[m. Try Again: '))
        player_counter += 1
print('You tried {} times to guess the correct number.'.format(player_counter))
