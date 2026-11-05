# Criar um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.

# nomeC = str(input('Digite o nome completo: '))
nomeC = 'Rafael Hiroshi Watanabe da Ponte Falcão'
print('Nome em maiúsculas: {}'.format(nomeC.upper()))
print('Nome em minúsculas: {}'.format(nomeC.lower()))
print('Total de letras (sem espaços): {}'.format(len(nomeC.replace(' ', ''))))
print('Quantidade de letras no primeiro nome: {}'.format(len(nomeC.split()[0])))