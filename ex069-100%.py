# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
from time import sleep

age = age_18counter = man_counter = w_under20 = persons = 0
sex = ' '
while True:
    age = int(input('Enter the age: '))
    sex = str(input('Enter the gender of this person [M/F]: ')).strip()[0]
    while sex not in 'MmFf':
        sex = str(input('This sex does not exist!! Type again [M/F]: ')).strip()[0]
    persons += 1
    if age >= 18:
        age_18counter += 1
    if sex in 'Mm':
        man_counter += 1
    else:
        if age < 20:
            w_under20 += 1
    asw = str(input('Do you want to continue? [Y/N]: '))
    while asw not in 'YyNn':
        asw = str(input('This option does not exist!!\nDo you want to continue? [Y/N]: ')).strip()[0]
    if asw in 'Yy':
        print('-=-' * 20)
        print('Creating new form...')
        print('-=-' * 20)
        sleep(4)
    elif asw in 'Nn':
        break
print('~' * 70)
if persons > 1:  # if there are 2 or more persons.
    print(f'From {persons} people registered.', end=' ')
    if age_18counter > 1:  # Persons above 18 years.
        print(f'There are {age_18counter} persons above 18-years-old.')
    elif age_18counter == 1:
        print(f'The is one person above 18-years-old.')
    elif age_18counter < 1:
        print('There is not a person above 18-years-old.')
    if man_counter > 1:  # if there are 2 or more men registered.
        print(f'\nThere are {man_counter} men registered', end=' ')
    elif man_counter < 1:
        print(f'\nThere is not man registered', end=' ')
    elif man_counter == 1:
        print(f'\nThere is one man registered', end=' ')
    if w_under20 > 1:  # if there are 2 or more women above 20-years-old.
        print(f'and there are {w_under20} women under 20-years-old.')
    elif w_under20 < 1:
        print(f'and there is not woman under 20-years-old')
    elif w_under20 == 1:
        print(f'and there is one woman under 20-years-old.')
elif persons == 1:  # if there is one person.
    print(f'From a {persons} registered person.', end=' ')
    if age_18counter > 1:  # Persons above 18 years
        print(f'There are {age_18counter} persons above 18-years-old.')
    elif age_18counter == 1:
        print(f'The is one person above 18-years-old.')
    elif age_18counter < 1:
        print('There is not a person above 18-years-old.')
    if man_counter > 1:  # if there are 2 or more men registered.
        print(f'\nThere are {man_counter} men registered', end=' ')
    elif man_counter < 1:
        print(f'\nThere is not man registered', end=' ')
    elif man_counter == 1:
        print(f'\nThere is one man registered', end=' ')
    if w_under20 > 1:  # if there are 2 or more women above 20-years-old.
        print(f'and there are {w_under20} women under 20-years-old.')
    elif w_under20 < 1:
        print(f'and there is not woman under 20-years-old')
    elif w_under20 == 1:
        print(f'and there is one woman under 20-years-old.')
print('~'*70)
