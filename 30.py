minutos = int(input('Digite a quantidade de minutos : '))

dias = minutos // 1440
resto = minutos % 1440
horas = resto // 60
resto_minutos = resto % 60 

print(f'A quantidade de minutos corresponde à : {dias} dias , {horas} horas e {resto_minutos} minutos')
