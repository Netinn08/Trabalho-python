numero = int(input("Digite um número inteiro: ")) 
if numero > 0:
    if numero % 2 == 0:
        print("O número é positivo e par.")
    elif numero % 3 == 0:
        print("O número é positivo e múltiplo de três.")
    else:
        print("O número é positivo, mas não é par nem múltiplo de três.")
elif numero < 0:
     if numero % 2 != 0:
         print("O número é negativo e ímpar.")
     else:
         print("O número é negativo, e par.")
else:
    print("O número é zero.")