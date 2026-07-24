"""

El Reto: El Evaluador de Operadores

Escribe un script en Python que cumpla con los siguientes tres bloques:
Bloque 1: Operadores Aritméticos y Cadenas

    Declara una variable numérica con los minutos totales (por ejemplo, 145).

    Utiliza la división entera (//) para calcular cuántas horas completas son y guárdala en una variable llamada horas.

    Utiliza el operador módulo (%) para calcular cuántos minutos sobrantes quedan y guárdala en una variable llamada minutos.

    Imprime el resultado en un formato claro (ej. "145 minutos equivalen a 2 horas y 25 minutos").

    Usa la multiplicación de cadenas (*) para imprimir una línea separadora formada por 30 guiones ("-").

Bloque 2: Operadores Comparativos (con texto y longitudes)

    Declara dos variables con palabras distintas (por ejemplo, "bici" y "avion").

    Realiza y muestra en consola una comparación alfabética directa entre ambas palabras (usando >).

    Realiza y muestra en consola una comparación basada en la longitud de ambas palabras utilizando len().

Bloque 3: Operadores Lógicos

    Crea una expresión lógica compleja utilizando números o comparaciones que involucre a los tres operadores lógicos (and, or, not) y al menos un paréntesis que altere el orden de evaluación.

    Guarda el resultado booleano (True o False) en una variable llamada evaluacion e imprímela.

Pega tu código aquí cuando lo tengas listo y lo analizamos paso a paso. ¡A programar!


"""
##intento 1 para tratar de entender
cont=0

valores_totales=int(input("Ingrese los minutos que desea convertir a horas: "))
ayuda=valores_totales

while valores_totales>60:
    valores_totales=valores_totales-60
    cont=cont+1


print("los minutos restantes son",valores_totales,"Y",ayuda,"Minutos son",cont,"Horas")

lapiz="hshsslsksks"
avion="NOse"

print((lapiz>avion))

print(len(lapiz))
print(len(avion))



