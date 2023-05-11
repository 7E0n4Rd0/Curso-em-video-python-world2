# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
woman_under20 = 0
older_a = 0
older_n = ''
soma = 0
for counter in range(1, 5):
    name = str(input('Enter the name of the {}° people: '.format(counter))).strip()
    age = int(input('Enter the age of the {}° people: '.format(counter)))
    sex = str(input('Enter the sex of the {}° people [M/F]: '.format(counter))).strip().upper()
    if counter == 1:
        older_n = name
        older_a = age
        older_s = sex
    else:
        if sex == 'F' and age < 20:
            woman_under20 += 1
        elif sex == 'M' and age > older_a:
            older_n = name
            older_a = age
    soma += age
    print('-=-'*20)
media = soma/4
print('The media of the age in the group is {:.1f} years;\nThe older man is {} and his age is {}\nand there are {} '
      'womens under 20 years old.'.format(media, older_n, older_a, woman_under20))