# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random, time

print('{:=^40}'.format(' JoKenPo '))
time.sleep(3)
print('\033[7;40mYou will choose rock or paper or scissors and I will choose and play too\033[m.')
time.sleep(4)
print('-=-'*10)
print('Jo')
time.sleep(1)
print('{:>10}'.format('Ken'))
time.sleep(1)
print('{:>20}'.format('Po'))
print('-=-'*10)
time.sleep(1)
computer = random.randint(1, 3)
print('''Choose:
[ 1 ] Rock
[ 2 ] Paper
[ 3 ] Scissors ''')
answ = int(input(''))
print('-=-'*10)
print('Loading...')
print('-=-'*10)
time.sleep(2)
if answ == 1 and computer == 3: # If the situation was Rock x Scissors
    print('You chosed Rock and I chosed Scissors: {}You Win{}!!!'.format('\033[32m', '\033[m'))
elif answ == 1 and computer == 2: # If the situation was Rock x Paper
    print('You chosed Rock and I chosed Paper: {}You Loose{}!!!'.format('\033[31m', '\033[m'))
elif answ == 2 and computer == 1: # If the situation was Paper x Rock
    print('You chosed Paper and I chosed Rock: {}You Win{}!!!'.format('\003[32m', '\033[m'))
elif answ == 2 and computer == 3: # If the situation was Paper x Scissors
    print('You chosed Paper and I chosed Scissors: {}You Loose{}!!!'.format('\033[31m', '\033[m'))
elif answ == 3 and computer == 1: # If the situation was Scissors x Rock
    print('You chosed Scissors and I chosed Rock: {}You Loose{}!!!'.format('\033[31m', '\033[m'))
elif answ == 3 and computer == 2: # If the situation was Scissors x Paper
    print('You chosed Scissors and I chosed Paper: {}You Win{}!!!'.format('\033[32m', '\033[m'))
elif answ == computer: # If the situation was the same option
    print('{}Draw{}!!! We choose the same option.'.format('\033[33m', '\033[m'))
elif answ != 1 or 2 or 3:
    print('{}ERROR{}!!! This Option does not exist!'.format('\033[31m', '\033[m'))
#This game is beautiful bro :D - 04/01/2023 - 10:09