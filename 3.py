valor_minutos = float(input("Informe o valor em minutos :"))

conversao_horas = valor_minutos // 60
minutos = valor_minutos % 60

print(f"O valor lido em  minutos é : {valor_minutos} min , o mesmo valor em horas e minutos é : {conversao_horas} horas e {minutos} minutos")
