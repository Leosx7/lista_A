numero_quatro_digitos = int(input('Digite um numero ( de 4 dígitos) : '))

millhar = numero_quatro_digitos // 1000
resto = numero_quatro_digitos % 1000
centena = resto // 100
resto_centena = resto % 100
dezena = resto_centena // 10
unidade = resto_centena % 10

soma = millhar + centena + dezena + unidade

print(f'O numero dígitado é : {numero_quatro_digitos} , e a soma dos seus caracteres é : {soma}  ')
