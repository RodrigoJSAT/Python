
"""

Asignación múltiple: Crea en una sola línea cuatro variables que almacenen: tu nombre (string), tu edad (entero), tu altura en metros (float) y si estás estudiando actualmente (booleano).

    Concatenación y funciones: Imprime una oración usando esas variables que combine texto y valores. Además, debes incluir en la impresión la longitud de tu nombre utilizando la función del sistema correspondiente.

    Conversión de tipos (Casting): Toma la variable de la altura, conviértela explícitamente a un tipo de datos string, imprímela y muestra en consola el tipo de dato resultante usando type().

    Tipado dinámico y anotaciones: Declara una variable con anotación de tipo estricta (por ejemplo, score: int = 100), pero luego asígnale un valor completamente diferente de otro tipo (como un string o un booleano). Finalmente, imprime el resultado de type() de esa variable para demostrar que Python no bloquea el cambio.
"""

nombre=input(str("Ingrese su nombre Porfavor:"))

edad=input(("Ingrese su edad Porfavor:"))

altura=input(("Ingrese su altura"))

estudio=input(("Esta usted estudiando actualmente"))


print("Hola",nombre,"Ya sabemos tus Datos como edad altura y si estudias o no si quiero verificar su informacion")

print("Aqui los datos introducidos:")

print("Nombre: ",nombre)

print("Edad: ",edad)
print("Altura: ",altura)
print("Estudia o No: ",estudio)

print(len(nombre))

altura=str

print(type(altura))


nombreF="Juanito"
nombreF="hola"

print(nombreF)

