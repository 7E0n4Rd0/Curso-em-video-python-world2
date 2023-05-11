# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
grade01 = float(input('Enter the first grade: '))
grade02 = float(input('Enter the second grade: '))
media = float(grade01 + grade02)/2
if media < 5.0:
    print('Your grade is {}{:.1f}{}, you are \033[31mREPROVED\033[m!'.format('\033[31m',media,'\033[m'))
elif 5.0 < media <= 6.9:
    print('Your grade is {}{:.1f}{}, you are in \033[33mREPECURATION\033[m!'.format('\033[33m',media,'\033[m'))
elif media >= 7.0:
    print('Your grade is {}{:.1f}{}, you are \033[32mAPROVED\033[m!'.format('\033[32m',media,'\033[m'))
