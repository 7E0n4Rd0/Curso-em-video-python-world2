# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
asw = str('x')
cheapestPtr = str()
counter = 1
all_purchases = higher1000 = cheapestP = 0
print('~'*40)
print('Z O N A M A')
print('~'*40)
while True:
    name = str(input(f'Enter the name of the {counter}° product: ')).strip().title()
    price = float(input(f'Enter the price of the {name}: R$'))
    if counter == 1 or price < cheapestP:
        cheapestPtr = name
        cheapestP = price
    if price > 1000:
        higher1000 += 1
    all_purchases += price
    asw = str(input('Do you want to continue? [Y/N]: ')).strip()[0]
    while asw not in 'YyNn':
        asw = str(input('Do you want to continue? [Y/N]: ')).strip()[0]
    if asw in 'Nn':
        break
    else:
        print('-=-'*20)
        counter += 1
print('=-='*20)
print(f'All purchases will cost R${all_purchases:.2f};')
print(f'There are {higher1000} products higher than R$1000,00 and')
print(f'The cheapest product was {cheapestPtr} costing R${cheapestP:.2f}.')
print('=-='*20)
