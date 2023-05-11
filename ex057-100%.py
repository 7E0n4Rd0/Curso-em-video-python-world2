# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = str(input('Enter your sex [M/F]: ')).upper()
tester = bool(False)
if sex == 'F':
    tester = True
elif sex == 'M':
    tester = True
while tester == False:
    sex = str(input('Invalid! Please, inform your sex [M/F]: ')).upper()
    if sex == 'F' or 'M':
        tester = True
print('Sex {} is registered.'.format(sex))
# Not done yet. - 04/08/2023 - 18:20
# Now I finished. - 04/08/2023 - 18:32
# There is another option that I can use in while. - 04/09/2023 - 08:12
'''while sex not in 'MmFf'():
	sex = str(input('Invalid! Please, inform your sex [M/F]: ')).upper()
'''
