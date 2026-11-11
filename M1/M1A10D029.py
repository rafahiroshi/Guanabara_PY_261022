v = int(input('Qual a velocidade do veículo? '))

if v > 80:
    print('Você foi multado! A velocidade máxima permitida é de 80 km/h.')
    multa = int((v - 80) * 7)
    print('O valor da multa é de R${:.2f}.'.format(multa))
else:
    print('Tudo certo! Continue dirigindo com segurança.')