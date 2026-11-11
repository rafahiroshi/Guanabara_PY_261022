import random

n = random.randint(1, 5)

nE = int(input('O computador pensou em um número entre 1 e 5. Tente adivinhar: '))

if nE == n:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O número pensado pelo computador foi {}.'.format(n))