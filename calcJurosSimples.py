capital = float(input("Insira o capital: "))
taxaJuros = float(input("Insira a porcentagem de taxa de juros: ")) / 100
tempo = float(input("Insira o tempo: "))
jurosSimples = capital * taxaJuros * tempo
print("O juros após esse período será de:", jurosSimples)