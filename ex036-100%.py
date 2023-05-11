# Exercício Python 36: escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salario do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salario ou então o empréstimo será negado.
house = float(input('What is the value of the house [R$]? '))
salary = float(input('Enter the value of your salary [R$]: '))
years = int(input('In how many years you will pay? '))
years = years * 12
loan = house / years
fee = (salary * 30) / 100
if loan > fee:
    print('The loan is \033[31mdenied\033[m,\033[31m because the monthly installment will be higher than 30% of the '
          'salary\033[m. The value will be \033[31mR${:.2f}\033[m'.format(loan))
elif loan <= fee:
    print('The loan is \033[32mallowed\033[m. The value will be \033[32mR${:.2f}\033[m.'.format(loan))
# I had some issues in this code and I realized that I did wrong in the Algorithm course, so I fixed the Algorithm
# exercise and in this exercise I have done corectly. - 03/11/2023 - 11:43
