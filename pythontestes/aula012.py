name = str(input('What is your name? ')).strip().capitalize()
if name == 'Gustavo':
    print('It is a beautiful name!')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Your name is very common in Brazil!')
elif name in 'Ana Cláudia Jessica Juliana':
    print('Beautiful female name.')
else:
    print('Your name is normal, {}'.format(name))
print('Have a nice day, {}'.format(name))
