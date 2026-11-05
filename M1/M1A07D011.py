largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print('A área da parede é de {:.2f} m² e para pintá-la você precisará de {:.2f} Litros de tinta'.format(area, tinta))