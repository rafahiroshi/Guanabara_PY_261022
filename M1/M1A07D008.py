m = float(input('Quantos metros você quer converter? '))

cm = m * 100
mm = m * 1000

print('{} metros é igual a {:.2f} centímetros e {:.2f} milímetros'.format(m, cm, mm))