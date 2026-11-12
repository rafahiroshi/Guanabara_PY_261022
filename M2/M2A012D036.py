vc = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
a = int(input('Por quantos anos você vai pagar? '))

p = vc / (a * 12)

if p > (s * 0.3):
    print('Empréstimo negado! O valor da prestação é de R${:.2f}, que excede 30% do seu salário.'.format(p))
else:
    print('Empréstimo aprovado! O valor da prestação é de R${:.2f}.'.format(p))