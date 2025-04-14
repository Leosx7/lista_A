nota1 = float(input('Digite o valor da nota 1 : '))
nota2 = float(input('Digite o valor da nota 2 : '))
nota3 = float(input('Digite o valor da nota 3 : '))
nota4 = float(input('Digite o valor da nota 4 : '))
peso_nota1 = float(input('Digite o peso da nota 1 :'))
peso_nota2 = float(input('Digite o peso da nota 2 :'))
peso_nota3 = float(input('Digite o peso da nota 3 :'))
peso_nota4 = float(input('Digite o peso da nota 4 :'))

media_ponderada = (nota1 * peso_nota1 + nota2 * peso_nota2 + nota3 * peso_nota3 + nota4 * peso_nota4) / (peso_nota1 + peso_nota2 + peso_nota3 + peso_nota4)

print(f'A media ponderada dos numeros é : {media_ponderada:.2f}')
