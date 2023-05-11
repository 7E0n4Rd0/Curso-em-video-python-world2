# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep

player_victory = False
player_victory_counter = 0
while True:
    print(f'{" Pair or Unpair [Game] ":~^40}')
    number = int(input('Enter some number: '))
    player = str(input('Pair or Unpair: [P/U] ')).upper().strip()[0]
    while player not in 'PpUu':
        player = str(input('Error, type again. Pair or Unpair: [P/U] ')).upper().strip()[0]
    if player in 'Pp':
        computer_str = 'U'
    elif player in 'Uu':
        computer_str = 'P'
    computer_n = randint(0, 10)
    s = number + computer_n
    asw = str('Loose')
    if s % 2 == 0 and player in 'Pp':
        player_victory = True
        player_victory_counter += 1
        asw = str('Win')
    elif s % 2 == 1 and player in 'Uu':
        player_victory = True
        player_victory_counter += 1
        asw = str('Win')
    else:
        player_victory = False
    print('-' * 40)
    sleep(1)
    print(f'You played \033[33m{number}\033[m and Computer played \033[35m{computer_n}\033[m. The sum is equal '
          f'\033[34m{s}\033[m')
    sleep(1)
    print(f'You chose \033[33m{player}\033[m and Computer chose \033[35m{computer_str}\033[m. \033[34mYou {asw}\033[m')
    sleep(1)
    print('-' * 40)
    sleep(1)
    if player_victory is False:
        break
    else:
        print("\033[7;40mLet's play again!!\033[m")
        sleep(3)
        print('-' * 40)
print(f'\033[31mGAME OVER!\033[m You won \033[31m{player_victory_counter}\033[m times in a row!!')
