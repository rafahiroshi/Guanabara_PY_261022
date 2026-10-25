import random
import math

cateto1 = random.uniform(1, 30)
print('Cateto 1: {:.2f}'.format(cateto1))

cateto2 = random.uniform(1, 30)
print('Cateto 2: {:.2f}'.format(cateto2))

# Usando Teorema de Pitágoras
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print('A hipotenusa dos catetos é: {:.2f}'.format(hipotenusa))