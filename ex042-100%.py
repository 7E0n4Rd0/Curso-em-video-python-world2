# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
print('-=-'*20)
print('Triangles')
print('-=-'*20)
a = int(input('Enter the value of the 1° side: '))
b =int(input('Enter the value of the 2° side: '))
c = int(input('Enter the value of the 3° side: '))
if a < b + c and b < a + c and c < a + b:
    print('This segments can form a triangle and',end='')
    if a == b == c:
        print('This triangle is Equilateral')
    elif a == b != c or a != b == c or a == c != b:
        print('This triangle is Isosceles.')
    elif a != b != c != a:
        print('This triangle is Escalene.')
else:
    print('This segments cannot form a triangle!')
