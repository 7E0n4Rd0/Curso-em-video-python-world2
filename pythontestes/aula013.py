# i = int(input('INÍCIO: '))
# f = int(input('FIM: '))
# p = int(input('PASSO: '))
# for c in range(i, f+1, p):
#   print(c)
# print('FIM')
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    # Eu posso escrever a soma assim: s = s + n ou assim: s += n
    s += n
print('O somátorio de todos os valores foi {}'.format(s))
