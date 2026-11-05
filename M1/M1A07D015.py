km = float(input('Quantos quilômetros você percorreu? '))
dias = int(input('Quantos dias você ficou com o carro? '))

custo = (km * 0.15) + (dias * 60)

print('O custo total do aluguel do carro é de R$ {:.2f}'.format(custo))