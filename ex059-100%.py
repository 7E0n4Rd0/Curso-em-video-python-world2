# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
number_01 = int(input('Enter the First number: '))
number_02 = int(input('Enter the Second number: '))
resp = int(0)
sleep(1)
print('=== [Menu] ===')
while resp != 5:
    resp = int(input('[ 1 ] sum\n[ 2 ] multiplication\n[ 3 ] higher \n[ 4 ] new numbersn\n[ 5 ] exit\n'))
    if resp == 1:
        print('The sum of {} and {} is equal to {}.'.format(number_01, number_02, (number_01 + number_02)))
    elif resp == 2:
        print('The multiplication of {} and {} is equal to {}.'.format(number_01, number_02, (number_01*number_02)))
    elif resp == 3:
        if number_01 > number_02:
            print('The First number: {} is bigger than Second number: {}.'.format(number_01, number_02))
        elif number_02 > number_01:
            print('The Second number: {} is bigger than First number: {}.'.format(number_02, number_01))
        else:
            print('They are the same number: {}.'.format(number_01))
    elif resp == 4:
        number_01 = int(input('Enter the First number: '))
        number_02 = int(input('Enter the Second number: '))
    elif resp == 5:
        print('Turning off...')
        sleep(2)
    else:
        print('This option does not exist, try again!')
    print('-=-'*10)
    sleep(1)
print('End')