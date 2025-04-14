idade_anos = int(input('Digite a idade em anos : '))
idade_meses = int(input('Digite a idade em meses : '))
idade_dias= int(input('Digite a idade em dias : '))

apenas_dias = (idade_anos * 365) + (idade_meses * 30) + idade_dias

print(f'A idade de uma pessoa expressa em anos, meses e dias em apenas em dias é : {apenas_dias} dias')
