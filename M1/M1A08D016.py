import math

x = float(input('Digite um número com ponto flutuante para ver sua parte inteira: '))
print('A parte inteira de {} é {}'.format(x, math.trunc(x)))