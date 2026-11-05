algo = input('Digite algo = ')
print('O tipo primitivo desse valor é', type(algo))

print('É alfanumérico' if algo.isalnum() else 'Não é alfanumérico')

print('É alfabético' if algo.isalpha() else 'Não é alfabético')

print('É ASCII' if algo.isascii() else 'Não é ASCII')

print('É decimal' if algo.isdecimal() else 'Não é decimal')

print('É dígito' if algo.isdigit() else 'Não é dígito')

print('É identificador' if algo.isidentifier() else 'Não é identificador')

print('É minúscula' if algo.islower() else 'Não é minúscula')

print('É numérico' if algo.isnumeric() else 'Não é numérico')

print('É imprimível' if algo.isprintable() else 'Não é imprimível')

print('É espaço' if algo.isspace() else 'Não é espaço')

print('É capitalizada' if algo.istitle() else 'Não é capitalizada')

print('É maiúscula' if algo.isupper() else 'Não é maiúscula')