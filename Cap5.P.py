invitados_vip=("Jeff Besos","Elon Musk","Donal Trump")

invitados_generales=("Juan","Pedro","John")

registro_de_entradas=[]

cont=0
while cont<=2:
    nombre=input("Ingrese su nombre: ")

    if nombre in invitados_vip:
        print(f"Bienvenido VIP {nombre} Esperamos que disfrute mucho")

        registro_de_entradas.append(nombre)

    elif nombre in invitados_generales:
        print(f"Bienvenido {nombre} Disfrute su estancia")

        registro_de_entradas.append(nombre)

    else:
        print(f"Lo sentimos el nombre: {nombre}") 
        print("No se encuentra en la lista")

    cont=cont+1


registro_de_entradas=sorted(registro_de_entradas) 
"""
print(f"Los invitados Fueron:{len(registro_de_entradas)}")
print("Sus Nombres Aqui:")
for i in registro_de_entradas:
    
    print(i)
"""    

for i in range(len(registro_de_entradas)):
    print(f"Invitado Numero {i+1} {registro_de_entradas[i]}")