# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
biggest_weight = float(0)
lower_weight = float(0)
for counter in range(1, 6):
    weight = float(input('Enter the weight of the {}° people: '.format(counter)))
    if counter == 1:
        biggest_weight = weight
        lower_weight = weight
    else:
        if weight > biggest_weight:
            biggest_weight = weight
        elif weight < lower_weight:
            lower_weight = weight
print('The lower weight is {}Kg and the biggest weight is {}Kg'.format(lower_weight, biggest_weight))
