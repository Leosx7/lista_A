horas = int(input('Digite a quantidade de horas : '))

semanas = horas // 168
resto = horas % 168
dias = resto // 24
resto_horas = resto % 24

print(f'A quantidade de horas corresponde à : {semanas} semanas , {dias} dias e {resto_horas} horas')
