ienes = float(input('Quantos ienes você tem na carteira para converter em dólares e reais? ¥ '))
dolares = ienes * 0.00639
reais = ienes * 0.031300

print('Com ¥ {:.2f} você pode comprar US$ {:.2f}'.format(ienes, dolares))
print('Com ¥ {:.2f} você pode comprar R$ {:.2f}'.format(ienes, reais))