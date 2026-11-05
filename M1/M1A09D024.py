# Crie um programa que leia o nome de uma cidade e diga se o nome da cidade é "SANTO" com boolean.

cidade = str(input('Digite o nome da cidade: ')).upper().split()

print(cidade[0] == 'SANTO')