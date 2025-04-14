numero_tres_digitos = int(input('Digite um numero ( de 4 dígitos) : '))

centena = numero_tres_digitos // 100
resto = numero_tres_digitos % 100
dezena = resto // 10
unidade = resto % 10

soma = centena + dezena + unidade

print(f'O numero dígitado é : {numero_tres_digitos} , e a soma dos seus caracteres é : {soma}  ')
