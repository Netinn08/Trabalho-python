nota = float(input("Insira a nota: "))
if nota >= 9:
    print("Nota A")
elif nota < 9 and nota >= 7.5:
    print("Nota B")
elif nota < 7.5 and nota >= 6:
    print("Nota C")
elif nota < 6 and nota >= 4:
    print("Nota D")
else:
    print("Nota F")