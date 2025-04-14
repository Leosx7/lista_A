valor_a = int(input('Digite o valor do coeficiente a : '))
valor_b = int(input('Digite o valor do coeficiente b : '))
valor_c = int(input('Digite o valor do coeficiente c : '))
valor_d = int(input('Digite o valor do coeficiente d : '))
valor_e = int(input('Digite o valor do coeficiente e : '))
valor_f = int(input('Digite o valor do coeficiente f : '))

valor_x = (valor_c*valor_e - (valor_b*valor_f)) // (valor_a*valor_e - (valor_b*valor_d))
valor_y = (valor_a*valor_f - (valor_c*valor_d)) // (valor_a*valor_e - (valor_b*valor_d))


print(f'O valor de x é : {valor_x} e o valor de y é :  {valor_y}')
