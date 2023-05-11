# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('-=-' * 20)
print('A T M')
print('-=-' * 20)
cell_50 = cell_20 = cell_10 = cell_1 = 0
withdraw = int(input('What is the amount you will withdraw? R$'))
while True:
    if withdraw >= 50:
        withdraw -= 50
        cell_50 += 1
    elif withdraw >= 20:
        withdraw -= 20
        cell_20 += 1
    elif withdraw >= 10:
        withdraw -= 10
        cell_10 += 1
    elif withdraw >= 1:
        withdraw -= 1
        cell_1 += 1
    else:
        break
print(f'R$50 Cells {cell_50};')
print(f'R$20 Cells {cell_20};')
print(f'R$10 Cells {cell_10} and')
print(f'R$1 Cells {cell_1}.')
# I had some issues to do this exercise, It's the last exercise and I need study more. 05/09/2023 - 21:15