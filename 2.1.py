"""
Ejercicio 1: Casting y Operaciones con Input

    Pide al usuario su año de nacimiento usando input() y guárdalo en una variable.

    Pide al usuario el año actual usando input() y guárdalo en otra variable.

    Importante: Como los valores que devuelve input() son siempre strings (str), debes convertirlos explícitamente a enteros (int).

    Calcula la edad restando ambos años, imprime el resultado y muestra en consola el tipo de dato de esa edad usando type().

Ejercicio 2: Asignación Múltiple y Longitudes

    En una sola línea, asigna tres palabras diferentes (por ejemplo, tres tecnologías o hobbies) a tres variables distintas (habilidad1, habilidad2, habilidad3).

    Imprime una oración estructurada que combine las tres variables.

    Imprime la suma de la longitud (len()) de las tres palabras para saber cuántos caracteres ocupan en total.

Ejercicio 3: Anotaciones de tipo y Tipado dinámico

    Declara una variable llamada saldo utilizando una anotación de tipo estricta para que sea un número flotante (float), asignándole un valor inicial (ej. 1500.50).

    Imprime su tipo inicial usando type().

    Ahora, rompe la regla de la anotación reasignando a saldo un valor de tipo booleano (True o False).

    Vuelve a imprimir el tipo de saldo con type() para comprobar cómo Python maneja el tipado dinámico en tiempo de ejecución.
"""

nacimiento,actual=input("ingrese El ano que nacio:"),input("ingrese El ano actual:")

nacimiento=int(nacimiento)
actual=int(actual)

edad=actual-nacimiento

print("Tu edad es ",edad)

juego,hobbie,nacionalidad=input("Ingresa tu juego favorito: "),input("Ingresa tu hobbie: "),input("Ingresa tu nacionalidad: ")

print("Hola soy jueanito Mi juego favorito es",juego,"Mi hobbie es",hobbie,"Y soy de nacionalidad",nacionalidad)

print(len(juego+hobbie+nacionalidad))


saldo =10098.903

print(type(saldo))


saldo=bool(saldo)

print(type(saldo))
