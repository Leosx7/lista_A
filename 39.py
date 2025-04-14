numero_a = int(input('Digite o número A : '))
numero_b = int(input('Digite o número B : '))
numero_c = int(input('Digite o número C : '))

valor_R = (numero_a + numero_b)** 2
valor_S = (numero_b + numero_c)** 2
valor_D = (valor_R + valor_S) // 2

print(f'O valor de A , B e C respectivamente é : {numero_a} ,{numero_b} e {numero_c}')
print(f'O resultado das expressões R e S respectivamente é : {valor_R} e {valor_S}')
print(f'O resultado da expressao D é : {valor_D}')
