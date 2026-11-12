edad_usuario = int(input("Dime tu edad: "))
estudiante = (input("¿Eres estudiante? : ")).lower()
dia =  (input("¿Para qué día?: ")).lower()

def cine(edad_usuario, estudiante, dia):
    result = ""

    if dia == "miercoles" or "miércoles":
        result = "El precio de su entrada es 4 "

    elif edad_usuario < 12:
        result = "El precio de su entrada es 4 "

    elif edad_usuario > 65:
        result = "El precio de su entrada es 5 "

    elif estudiante == "si":
        result = "El precio de su entrada es 5,6  "

    else:
        result = "El precio de su entrada es 8 "
    return result

print(cine(edad_usuario, estudiante, dia))