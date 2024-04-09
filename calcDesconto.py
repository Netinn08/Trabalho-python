valor = float(input("Digite o valor: "))
desconto = float(input("Digite a porcentagem do desconto: ")) / 100
precoFinal = valor - (valor * desconto)
print("O preço com desconto será:", precoFinal)