
numerador1 = int(input("Digite o numerador da primeira fração: "))
denominador1 = int(input("Digite o denominador da primeira fração: "))

numerador2 = int(input("Digite o numerador da segunda fração: "))
denominador2 = int(input("Digite o denominador da segunda fração: "))


numerador_resultado = (numerador1 * denominador2) + (numerador2 * denominador1)
denominador_resultado = denominador1 * denominador2

print(f"A soma das frações é: {numerador_resultado}/{denominador_resultado}")
