nombre=[]

categoria=[]

precio=[]

cantidad=[]

diccionario={
    "Producto": nombre,
    "key1": categoria,
    "key2": precio,
    "key3": cantidad
}

print("OPCIONES:")
print("1: Seguir Agregando Productos")
print("Salir: Dejar de agregar Productos")

continuacion=input()


while continuacion!="Salir":

    print("Ingrese Los datos del Producto:")

    Producto=input("Ingrese el nombre:")
    
    
    Categoria=input("Categoria:")

    if Categoria =="electronica":
        print("Categoria Encontrada")
        

    
    elif Categoria=="ropa":
        print("Categoria Encontrada")

    elif Categoria=="Alimentos":
        print("Categoria Encontrada")
                
    elif Categoria=="hogar":
        print("Categoria Encontrada")


    else:
        print("No se aceptan esos productos")    
        Categoria=input("Categoria:")
        
        
    nombre.append(Producto)

    categoria.append(Categoria)

    valor=input("Precio:")
    precio.append(valor)

    unidades=input("Cantidad:")
    cantidad.append(unidades)

    print("OPCIONES:")
    print("1: Seguir Agregando Productos")
    print("Salir: Dejar de agregar Productos")

    continuacion=input()

    