valor_mercadoria = int(input('Digite o valor da mercadoria (em R$) : '))

divisao = valor_mercadoria // 3
resto_divisao = valor_mercadoria % 3
entrada = divisao + resto_divisao
parcerla1 = divisao
parcerla2 = divisao

print(f'O valor da mercadoria é : {valor_mercadoria} R$')
print(f'O valor da entrada é : {entrada} R$ , da primeira parcela : {parcerla1} R$ e da ultima parcela é : {parcerla2} R$')
