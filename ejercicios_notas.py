nota = float(input("Dime tu nota: "))

if nota > 10:
    print("Incorrecto\n")

elif nota >= 9:
    print("Sobresaliente\n")

elif nota >= 7:
    print("Notable\n")

elif nota >= 6:
    print("Bien\n")

elif nota >= 5:
    print("Suficiente\n")

elif nota >= 0:
    print("Isuficiente\n")

else:
    print("Incorrecto\n")