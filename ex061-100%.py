# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Fórmula de P.A: an = a1 + (n-1)*r -> Soma dos termos da P.A: Sn = (a1 + an)*n/2
print('{:=^40}'.format(' Arithmetic Progression '))
first_term = int(input('Enter the value of the First term: '))
argument = int(input('Enter the value of the Argument: '))
print('-=-'*20)
count = 1
while count <= 10:
    an = first_term + (count - 1)*argument
    print('a{:02} = {} + ({:02} - 1)*{} = {:02}'.format(count, first_term, count, argument, an))
    count += 1
print('-=-'*20)
print('END!')