# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print('{:=^40}'.format(' Multiplication Table '))
number = int(input('Enter some number to make the Multiplication Table: '))
print('-=-'*10)
for count in range(1, 11):
    print('{} x {:2} = {}'.format(number, count ,count*number))
print('-=-'*10)
