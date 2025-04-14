valor_saque = int(input('Digite o valor a ser sacado : '))

cinquenta = valor_saque // 50
resto = valor_saque % 50
dez = resto // 10 
resto_dez = resto % 10
cinco = resto_dez // 5
resto_cinco = resto_dez % 5
um = resto_cinco // 1 

print(f'O valor sacado foi : {valor_saque} R$')
print(f'E a distribuição das notas fica assim : {cinquenta} notas de 50 R$ , {dez} notas de 10R$ , {cinco} notas de cinco e {um} notas de 1R$')
