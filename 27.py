segundos = int(input('Digite a quantidade de segundos : '))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
resto_segundos = resto % 60

print(f'A quantidade de segundos corresponde à : {horas} horas , {minutos} minutos e {resto_segundos} segundos')
