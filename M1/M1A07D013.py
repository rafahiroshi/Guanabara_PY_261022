salarioAntigo = float(input('Digite o salário que terá o reajuste: R$ '))
salarioNovo = salarioAntigo + (salarioAntigo * 0.15)

print('O salário que era R$ {:.2f}, passa a ser R$ {:.2f} com o reajuste de 15%'.format(salarioAntigo, salarioNovo))