# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
product_price = float(input('Enter the amount of purchases: R$ '))
payment = int(input('''How would you like to pay?
[1] Cash/Check 
[2] Cash Card
[3] Up to 2x on the card
[4] 3x or more on the card
'''))
print('-=-'*10)
if payment == 1:
    print('You choosed Cash/Check, so you got 10% off.\nThe bill will cost R${:.2f}.'.format(product_price-(product_price*10/100)))
elif payment == 2:
    print('You choosed Cash Card, so you got 5% off.\nThe bill will cost R${:.2f}.'.format(product_price-(product_price*5/100)))
elif payment == 3:
    print('You choosed up to 2x on the card.\nThe bills will cost 2x R${:.2f}'.format(product_price/2))
elif payment == 4:
    more_card = int(input('''You chosed 3x or more on the card.
[1] 3x on the card
[2] another option
'''))
    if more_card == 2:
        card_payment = int(input('Please, enter the number of times you would like to split: '))
        print('You choosed {}x on the card, you got 20% of fees.\nThe bills will cost {}x R${:.2f}'.format(card_payment, card_payment, (product_price/card_payment)*1.20))
    elif more_card == 1:
        print('You choosed 3x on the card, you got 20% of fees.\nThe bills will cost 3x R${:.2f}'.format((product_price/3)*1.20))
    else:
        print('This option does not exist!!!')
else:
    print('This option does not exist!!!')