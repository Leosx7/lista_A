#Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos
valor_horas = float(input("Informe o valor em horas : "))
valor_minutos = float(input("Informe o valor em minutos :"))

conversao_minutos = valor_horas * 60
minutos = conversao_minutos + valor_minutos

print(f"O valor lido em horas é : {valor_horas} h  e minutos é : {valor_minutos} min o mesmo valor lido apenas em minuto é equivalente a : {minutos}min")
