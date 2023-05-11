n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
# Printing a massage using fstrings:
print(f'A soma vale {s}')
# Another examples of fstrings
nome = 'José'
idade = 33
salario = 937.35
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
