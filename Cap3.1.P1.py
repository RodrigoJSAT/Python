calificaciones=[]


cont=0
contador_60=0
while cont<6:
    cal=input("INGRESE SUS CALIFICACIONES:")
    cal=int(cal)
    calificaciones.append(cal)
    cont=cont+1
    if cal<60:
        contador_60=contador_60+1
        print("Estas en riesgo tienes una calificacion menor que 60")
        print(f"Llevas una cantidad de:{contador_60} Calificaciones Menor que 60")

calificaciones.sort()
print(calificaciones)

nuevas=sorted(calificaciones,reverse=True)
print(nuevas)
print(f"Registraste la cantidad de {len(calificaciones)} Calificaciones")



print(f"La Calificacion Mas alta Fue: {max(calificaciones)}")

print(f"La Calificacion Mas Baja Fue: {min(calificaciones)}")

promedio=sum(calificaciones)/len(calificaciones)

print(f"SU PROMEDIO ES:{promedio}")

print(f"SUS TRES MEJORES CALIFICACIONES FUERON {nuevas[:3]}")


contador2=0
for i in calificaciones:
    print(f"Calificacion Numero: {contador2}: {i}")
    contador2=contador2+1