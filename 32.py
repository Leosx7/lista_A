numero_tres_digitos = int(input('Digite um numero ( de até 3 dígitos) : '))

centena = numero_tres_digitos // 100
resto = numero_tres_digitos % 100
dezena = resto // 10
unidade = resto % 10

inverso = unidade * 100 + dezena * 10 + centena
diferenca = numero_tres_digitos - inverso

print(f'A diferença de {numero_tres_digitos} e {inverso} é : {diferenca} ')
