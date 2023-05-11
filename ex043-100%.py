# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
# Fórmula: IMC = Peso/Altura²
print('-=-'*20)
print('Índice de Massa Corporal (IMC)')
print('-=-'*20)
weight = float(input('Enter your weight [Kilo]: '))
height = float(input('Enter your height [Meters]:'))
imc = weight/(height**2)
print('-=-'*10)
print('Imc = {:.2f}\nStatus: '.format(imc), end='')
if imc < 18.5:
    print('Under the weight')
elif 18.5 <= imc < 25:
    print('Ideal weight')
elif 25 <= imc < 30:
    print('Overweight')
elif 30 <= imc < 40:
    print('Obesity')
else:
    print('Morbid obesity')
