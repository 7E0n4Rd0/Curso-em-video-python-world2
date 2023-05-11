# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('{:~^38}'.format(' Multiplication Table '))
while True:
    counter = 1
    number = int(input('Enter some number: '))
    if number < 0:
        break
    print(f'{"-=-"}'*20)
    while counter <= 10:
        print(f'{number:02} x {counter:02} = {number*counter:02}')
        counter += 1
    print(f'{"-=-"}'*20)
print('Bye Bye')
print(f'{"~"}'*60)
