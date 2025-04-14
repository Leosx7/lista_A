numero_anos_fumando = int(input('Digite a quantidade de anos que fuma : '))
numero_cigarros_dias = int(input('Digite a quantidade de cigarros por dia : '))
preco_carteria = float(input('Digite o preço da carteira (em R$) : '))

anos_em_dias = numero_anos_fumando * 365
quantidade_cigarros = anos_em_dias * numero_cigarros_dias
quantidade_carteira = quantidade_cigarros // 20
gasto = quantidade_carteira * preco_carteria

print(f'A quantidade de dinheiro gasta é : {gasto} R$')
