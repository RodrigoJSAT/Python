lista_de_compras=[]
i=1


while i< 4:
    productos=input("Ingrese un producto para agregar: ")
    lista_de_compras.append(productos)
    i=i+1

lista_de_compras[0]=lista_de_compras[0].rstrip()
print(f"Tu Primer Producto Ingresado Fue {lista_de_compras[0].title()}")

lista_de_compras.insert(1,"Leche de soya")

print(lista_de_compras)

producto_comprado=lista_de_compras.pop(-1)

print(f"Ya compre la {producto_comprado.title()}")

print(lista_de_compras)


lista_de_compras.remove("Leche de soya")



print(lista_de_compras)

del lista_de_compras[0]

for i in lista_de_compras:
    print(i)
    print(i)


print(len(lista_de_compras))