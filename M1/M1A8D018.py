# Usando a série de Taylor para calcular o seno, cosseno e tangente de um ângulo em graus

x = float(input('Digite um ângulo para calcular o seno, cosseno e tangente: '))

if x < -180 or x > 180:
    y = x % 360
else:
    y = x

if y > 180:
    y = y - 360
print('O ângulo ajustado é: {}'.format(y))

pi = 3.141592653589793
senoR = (y * pi) / 180

# Utilizando a série de Taylor para calcular o seno 15 vezes, ou seja, foi utilizado 15 termos da série de Taylor para calcular o seno do ângulo em radianos
seno = senoR - ((senoR**3) / (3*2*1)) + ((senoR**5) / (5*4*3*2*1)) - ((senoR**7) / (7*6*5*4*3*2*1)) + ((senoR**9) / (9*8*7*6*5*4*3*2*1)) - ((senoR**11) / (11*10*9*8*7*6*5*4*3*2*1)) + ((senoR**13) / (13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((senoR**15) / (15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((senoR**17) / (17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) - ((senoR**19) / (19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4 *3 *2 *1)) + ((senoR**21) / (21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4 *3 *2 *1)) - ((senoR**23) / (23*22*21*20*19*18*17*16*15*14*13*12*11 *10 *9 *8 *7 *6 *5 *4 *3 *2 *1)) + ((senoR**25) / (25*24*23*22*21*20*19*18*17 *16 *15 *14 *13 *12 *11 *10 *9 *8 *7 *6 *5 *4 *3 *2 *1)) - ((senoR**27) / (27*26*25*24*23*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)) + ((senoR**29) / (29*28*27*26*25*24*23*22*21*20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1))

print('O seno do ângulo {} é: {}'.format(x, seno))