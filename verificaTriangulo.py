lA = float(input("Insira o tamanho do lado A: "))
lB = float(input("Insira o tamanho do lado B: "))
lC = float(input("Insira o tamanho do lado C: "))

if lA >= lB + lC or lB >= lC + lA or lC >= lA + lB :
    print("O triângulo não é possível")
else:
    print("O triângulo é possível")
    if lA == lB and lA == lC:
        print("O triângulo é equilátero (todos os lados iguais)")
    elif lA == lB or lA == lC or lB == lC:
        print("O triângulo é isósceles (dois lados iguais)")
    elif lA != lB and lA != lC and lB != lC:
        print("O triângulo é escaleno (três lados distintos)")