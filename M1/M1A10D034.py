s = float(input('Digite o salário do funcionário: R$ '))

if s > 1250:
    print('O salário do funcionário com 10% de aumento será R$ {:.2f}'.format(s + (s * 10 / 100)))
else:
    print('O salário do funcionário com 15% de aumento será R$ {:.2f}'.format(s + (s * 15 / 100)))