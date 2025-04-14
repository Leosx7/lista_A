import math
x1 = float(input('Digite o valor de x1 : '))
x2 = float(input('Digite o valor de x2 : '))
y1 = float(input('Digite o valor de y1 : '))
y2 = float(input('Digite o valor de y2 : '))

diferenca_x = (x2 - x1)**2
diferenca_y = (y2 - y1)**2
soma_diferencas = diferenca_x + diferenca_y
distancia = math.sqrt(soma_diferencas)

print(f'A distância entre os pontos é : {distancia:.2f}')
