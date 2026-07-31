"""
El Reto Práctico: Gestor de Tareas Diarias

Siguiendo nuestra regla de hacer cosas útiles y prácticas, vamos a crear un pequeño gestor de tareas para poner a prueba las listas:

    Crea una lista llamada tareas que contenga inicialmente 3 cosas que tengas que hacer hoy (ej. ["Estudiar Python", "Limpiar la habitación", "Comprar agua"]).

    Añade una nueva tarea a esa lista utilizando el método de Python diseñado para agregar elementos al final (append).

    Muestra en consola únicamente la primera tarea y la última tarea de tu lista (recuerda que en programación las posiciones empiezan a contar desde el 0).

    Imprime el total de tareas que tienes anotadas utilizando la función del sistema len().



"""
lista=[]
cont=0

print("Bienvenido al almacen de tareas")

print("Ingrese el numero de tareas que tiene que hacer: ")
cosas_que_hacer=int(input(":"))


while cont!=cosas_que_hacer:
    tareas=str(input("Ingrese sus tareas a apuntar:"))
    lista.append(tareas)

    cont=cont+1


print(f"Ya termino de ingresar sus tareas que en total fueron:{cont} Tareas:")

print("TAREAS GUARDADAS: ")


for i in lista:
    print(i)

print("Numero de cada tarea: ")

for hola in range (len(lista)):
    print(hola)


    
borrar=input("Ingrese el numero de la tarea que desea borrar y si no quiere ingrese no: ")

if borrar != "no":
    borrar=int(borrar)


eliminar=lista.pop(borrar)

print(f"elimino con exito la tarea {eliminar}")

for i in lista:
    print(lista)
