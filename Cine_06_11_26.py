

edad_usuario = int(input("Dime tu edad: "))
estudiante = (input("¿Eres estudiante? : ")).lower()
dia =  (input("¿Para qué día?: ")).lower()

if dia == "miercoles":
    print("El precio de su entrada es 4 ")

elif edad_usuario < 12:
    print("El precio de su entrada es 4 ")

elif edad_usuario > 65:
    print("El precio de su entrada es 5 ")

elif estudiante == "si":
    print("El precio de su entrada es 5,6  ")

else:
    print("El precio de su entrada es 8 ")