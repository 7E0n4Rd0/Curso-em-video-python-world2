# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
# Previous code
print('{:=^40}'.format(' Arithmetic Progression '))
first_term = int(input('Enter the value of the First term: '))
common_difference = int(input('Enter the value of the Common difference: '))
print('-=-'*20)
count = 1
more = 10
term = 0
#while count <= 10:
#    an = first_term + (count - 1)*common_difference
#    print('a{:02} = {:02}'.format(count, an))
#    count += 1
#print('-=-'*20)
#term = int(input('How much terms do want? [Type 0 to end the programm] '))
#while term > 0:
#    end = count + term
#    while count < end:
#        an = first_term + (count - 1)*common_difference
#        print('a{:02} = {:02}'.format(count, an))
#        count += 1
#    print('-=-'*20)
# Optimizing the code
while more != 0:
    term += more
    while count <= term:
        an = first_term + (count - 1)*common_difference
        print('a{:02} = {:02}'.format(count, an))
        count += 1
    print('-=-'*20)
    more = int(input('How much terms do want? [Type 0 to end the programm] '))
print('The programm showed {} terms.'.format(count - 1))
print('END!')