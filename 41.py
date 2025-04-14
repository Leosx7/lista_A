custo_fabrica = float(input('Digite o custo de fábrica (em R$) : '))
porcentagem_distribuidor = float(input('Digite o valor da porcentagem distribuidor : '))
porcentagem_impostos = float(input('Digite o valor da porcentagem imposto : '))

distribuidor = (custo_fabrica) * (porcentagem_distribuidor / 100)
impostos = (custo_fabrica * (porcentagem_impostos / 100))
custo_consumidor = custo_fabrica + distribuidor + impostos

print(f'O custo do carro ao consumidor é : { custo_consumidor} R$')
