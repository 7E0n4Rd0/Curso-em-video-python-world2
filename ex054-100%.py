# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
above_age = 0
under_age = 0
for counter in range(1, 8):
    year_birth = int(input('Enter the year born of the {}° people: '.format(counter)))
    age = 2023 - year_birth
    if age > 21:
        above_age += 1
    elif age < 21:
        under_age += 1
print('There are {} people above the age and {} under the age.'.format(above_age, under_age))
