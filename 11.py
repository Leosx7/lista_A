numero_tres_digitos = int(input('Digite um numero ( de até 3 dígitos) : '))

centena = numero_tres_digitos // 100
resto = numero_tres_digitos % 100
dezena = resto // 10
unidade = resto % 10

inverso = unidade * 100 + dezena * 10 + centena

print(f'O numero digitado é : {numero_tres_digitos} e o seu inverso é : {inverso}')
