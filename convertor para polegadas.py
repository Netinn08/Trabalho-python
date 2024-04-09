medida = float(input("Insira o valor da medida: "))
tipoMedida = int(input("A medida inserida é em:\n[1] Milhas\n[2] Polegadas\n[3] Pés\n[4] Centímetros\n[5] Metros\n[6] Quilômetros\nInsira o número correspondente: "))
medidaEmM = 0

if tipoMedida == 1:
    medidaEmM = medida * 1609
elif tipoMedida == 2:
    medidaEmM = medida / 39.37
elif tipoMedida == 3:
    medidaEmM = medida / 3.281
elif tipoMedida == 4:
    medidaEmM = medida / 100
elif tipoMedida == 5:
    medidaEmM = medida
elif tipoMedida == 6:
    medidaEmM = medida * 1000

if tipoMedida != 1:
    print("O valor em milhas será: ", medidaEmM / 1609)
if tipoMedida != 2:
    print("O valor em polegadas será: ", medidaEmM * 39.37)
if tipoMedida != 3:
    print("O valor em pés será: ", medidaEmM * 3.281)
if tipoMedida != 4:
    print("O valor em centímetros será: ", medidaEmM * 100)
if tipoMedida != 5:
    print("O valor em metros será: ", medidaEmM)
if tipoMedida != 6:
    print("O valor em quilômetros será: ", medidaEmM / 1000)

