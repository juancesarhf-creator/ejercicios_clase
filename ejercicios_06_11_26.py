hobbies =["videojuegos", "baloncesto", "leer"]
print(hobbies[1])
print(hobbies[2])
print(hobbies[-1])

et = float(input("\nIngrese el numero de espacio total del disco duro: "))
eo = float(input("Ingrese el numero de espacio ocupado: "))

if et > eo:
    print("guardar")

elif  et == eo:
    print("no hay espacio")

else:
    print("error")

