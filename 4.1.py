"""

Reglas y requisitos:

    Inicia con una lista vacía llamada historial.

    Permite ingresar datos: Usa un bucle para pedirle constantemente al usuario que escriba una acción, palabra o texto.

    Guarda con .append(): Cada vez que el usuario escriba una acción normal, guárdala automáticamente al final de la lista historial.

    Deshaz con .pop(): Si el usuario escribe exactamente la palabra "deshacer", el programa debe sacar el último elemento de la lista usando .pop(), mostrar un mensaje indicando qué acción se eliminó, y actualizar el estado.

    Muestra el estado: Después de cada cambio (ya sea agregar o deshacer), imprime la lista actual para ver cómo va quedando el historial.


"""

historial=[]


cosas_que_buscar=int(input("Cuantas Cosas desea guardar en su historial: "))

cont=0
while cont < cosas_que_buscar:
    cosas=input("Ingrese lo que desea guardar: ")
    historial.append(cosas)
    cont=cont+1

    print("Estado de la lista: ")
    for i in historial:
        print(i)

    seguir=input("Desea seguir agregando cosas o quiere parar: ")

    if seguir!="Si":
        break

    elimirar=input("Desea eliminar una tarea escriba Deshacer si haci lo desea: ")

    if elimirar=="Deshacer":
        elimi=historial.pop(-1)

    print("Estado de la lista: ")
    for i in historial:
        print(i)