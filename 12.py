
salario_trabalhador = float(input('Digite o valor do salário do trabalhador : '))

porcentagem = 25 / 100
aumento = salario_trabalhador * porcentagem
salario_novo = salario_trabalhador + aumento

print(f'O salário antes do aumento é : {salario_trabalhador} e o seu salário após o aumento é : {salario_novo}')
