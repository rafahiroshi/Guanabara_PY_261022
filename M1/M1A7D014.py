celsius = float(input('Digite a temperatura em °C: '))

fahrenheit = (celsius * 1.8) + 32
# Também poderia ser: fahrenheit = (celsius * 9) / 5 + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(celsius, fahrenheit))