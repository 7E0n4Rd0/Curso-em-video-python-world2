# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# Fórmula de P.A: an = a1 + (n-1)*r -> Soma dos termos da P.A: Sn = (a1 + an)*n/2
print('{:=^40}'.format(' Progressão Aritmética '))
first_term = int(input('Enter the First term (a1) of the P.A: '))
argument = int(input('Enter the argumnet (r) of the P.A: '))
print('-=-'*10)
for counter in range(1, 11):
    an = first_term + (counter-1)*argument
    print('a{:02} = {} + ({:02} - 1)*{} -> {}'.format(counter, first_term, counter, argument, an))
print('-=-'*10)
