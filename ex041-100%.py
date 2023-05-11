# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, conforme a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
actual_year = date.today().year
born_year = int(input('Birth year: '))
age = actual_year - born_year
print("The athlete's age is {}.".format(age))
if age <= 9:
    print('Your category is Little.')
elif 10 <= age <= 14:
    print('Your category is Childish.')
elif 15 <= age <= 19:
    print('Your category is Junior.')
elif 20 <= age <= 25:
    print('Your category is Senior.')
else:
    print('Your category is Master.')
