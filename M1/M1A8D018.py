# Utilizando a série de Taylor para calcular o seno, cosseno e tangente de um ângulo em graus com redução de ângulo para o intervalo [-180, 180]
#Entrada e formatação de números com float() e .format().
#Redução de ângulos utilizando %.
#Estruturas condicionais com if, else, and e or.
#Conversão de graus para radianos.
#Cálculo do seno e cosseno com 15 termos da série de Taylor.
#Cálculo da tangente a partir do seno e cosseno.
#Tratamento dos ângulos em que a tangente é indefinida.
#Sem importar bibliotecas.

x = float(input('Digite um ângulo para calcular o seno, cosseno e tangente: '))
print('O ângulo escolhido foi: {:.2f}'.format(x))

# Reduzindo o ângulo para o intervalo [-180, 180]
if x < -180 or x > 180:
    y = x % 360
else:
    y = x

if y > 180:
    y = y - 360
# print('O ângulo ajustado é: {}'.format(y))

pi = 3.141592653589793
# Convertendo o ângulo para radianos com o ângulo já reduzido
radianoReduzido = (y * pi) / 180

# Utilizando 15 termos da série de Taylor para calcular o seno do ângulo em radianos
sen = radianoReduzido - ((radianoReduzido**3) / (3*2*1)) + ((radianoReduzido**5) / (5*4*3*2*1)) - ((radianoReduzido**7) / (7*6*5*4*3*2*1)) + ((radianoReduzido**9) / (9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**11) / (11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**13) / (13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**15) / (15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**17) / (17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**19) / (19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4 *3 *2 *1)) + ((radianoReduzido**21) / (21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4 *3 *2 *1)) - ((radianoReduzido**23) / (23*22*21*20*19*18*17*16*15*14*13*12*11 *10 *9 *8 *7 *6 *5 *4 *3 *2 *1)) + ((radianoReduzido**25) / (25*24*23*22*21*20*19*18*17 *16 *15 *14 *13 *12 *11 *10 *9 *8 *7 *6 *5 *4 *3 *2 *1)) - ((radianoReduzido**27) / (27*26*25*24*23*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**29) / (29*28*27*26*25*24*23*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1))

print('O seno do ângulo {:.2f} é: {}'.format(x, sen))

cos = 1 - ((radianoReduzido**2) / (2*1)) + ((radianoReduzido**4) / (4*3*2*1)) - ((radianoReduzido**6) / (6*5*4*3*2*1)) + ((radianoReduzido**8) / (8*7*6*5*4*3*2*1)) - ((radianoReduzido**10) / (10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**12) / (12*11*10*9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**14) / (14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**16) / (16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**18) / (18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**20) / (20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**22) / (22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**24) / (24*23*2*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((radianoReduzido**26) / (26*25*24*23*2*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((radianoReduzido**28) / (28*27*26*25*24*23*2*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1))

print('O cosseno do ângulo {:.2f} é: {}'.format(x, cos))

if y != -90 and y != 90:
    tang = sen / cos

    print('A Tangente do ângulo {:.2f} é: {}'.format(x, tang))
else:
    print('A Tangente do ângulo {:.2f} é indefinida'.format(x))