# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
phrase = str(input('Enter some phrase: ',)).strip().upper().split()
phrase = str(''.join(phrase))
palindrome_s = str(''.join(phrase[::-1]))
for i in range(len(phrase), 0, -1):
    for j in range(len(phrase), 1, -1):
        if palindrome_s[i:j] == phrase[i:j]:
            palindrome_b = True
        else:
            palindrome_b = False
print('The Palindrome: {}'.format(palindrome_s))
print('The Phrase: {}'.format(''.join(phrase)))
print('This phrase is Palindrome: {}'.format(palindrome_b))

# I think it is wrong, I'm bad in manipulation strings. - 04/06/2023 - 10:04
# I'll redo one more time. - 04/06/2023 - 10:06
# HOLLY FUCK!!! I Redid this shit and his works, FUCK YEAH!!! - 04/06/2023 - 10:33