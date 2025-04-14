idade_dias= int(input('Digite a idade em dias : '))

anos = idade_dias // 365
resto = idade_dias % 365
meses = resto // 30
dias = resto % 30

print(f'A idade de uma pessoa expressa em dias , em anos , meses e dias é : {anos} anos , {meses} meses e  {dias} dias')
