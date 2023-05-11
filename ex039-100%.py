# Exercício Python 39: faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
year_born = int(input('Enter the year were you born: '))
age = int(2023 - year_born)
print('You have {} years old.'.format(age))
if age < 18:
    print('You are under than 18 years, so you \033[31mcannot enlist in the army\033[m.\n'
          '\033[31m{}\033[m years left to enlist.'.format(18-age))
    print('You will enlist in {}'.format((18+year_born)))
elif age == 18:
    print('You have the age to \033[32menlist in the army\033[m.')
elif age > 18:
    print('You are above to enlist.\nit is been \033[37m{}\033[m years since you should have enlisted '
          'in \033[37m{}\033[m'.format((age-18), 18+year_born))
