precoAntigo = float(input('Digite o preço do produto que vai ser reajustado: R$ '))

precoNovo = precoAntigo - (precoAntigo * 0.05)
# Também poderia ser feito assim: precoNovo = precoAntigo * 0.95

print('O preço do produto que era R$ {:.2f} com o reajuste de 5% passou a ser R$ {:.2f}'.format(precoAntigo, precoNovo))