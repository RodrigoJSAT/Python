list=["Juan","Pedro","Mohamed"]


print(f"{list[0].title()} Estas invitado")

print(f"{list[1].title()} Estas invitado")

print(f"{list[2].title()} Estas invitado")


print(f"{list[0].title()} No Podra asistir a la fiesta")

invitado="Felix"

list[0]=invitado

print(f"{list[0].title()} Estas invitado")

print(f"{list[1].title()} Estas invitado")

print(f"{list[2].title()} Estas invitado")

print("Encontre una mesa mas grande abran mas invitados: ")

list.insert(0,"Turin Turan")

list.insert(3,"Turan")

list.insert(-1,"Turin")

print(f"{list[0].title()} Estas invitado")

print(f"{list[1].title()} Estas invitado")

print(f"{list[2].title()} Estas invitado")

print(f"{list[3].title()} Estas invitado")

print(f"{list[4].title()} Estas invitado")

print(f"{list[5].title()} Estas invitado")

list.pop(0)


print(f"{list[0].title()} lamento eliminarte")

list.pop(1)

print(f"{list[1].title()} lamento eliminarte")


list.pop(2)

print(f"{list[2].title()} lamento eliminarte")





print(f"{list[0].title()} Estas invitado")

print(f"{list[1].title()} Estas invitado")


del list[0]
del list[1]

print(list)
