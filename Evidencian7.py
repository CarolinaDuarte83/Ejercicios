

"""Ejercicios Listas:
Crear cuatro listas:
1. Con los nombres de su familia.
2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
3. Con los nombres de ciudades que hayan visitado.
4. Con las fechas y nombres de eventos importantes de su vida.
Luego:
1. Ordenar alfabéticamente la lista de los nombres de familia.
2. Ordenar ascendentemente la lista de temperaturas.
3. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
4. Quitar de la lista de los nombres de familia, a tus abuelos.
5. Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.
6. Mostrar todas las listas.

Ejercicios Tuplas:
Crear tres tuplas con datos random.
Crear una lista que las contenga y mostrarla.

Ejercicio Diccionarios:
Crear el siguiente diccionario:
 Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)
 Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
Ambos deben ser mostrados.

ACLARACIÓN:
Los datos no deben ser reales."""

Nombre_Familia= ["Tomas", "Agustin", "Carolina", "Maria Ester", "Eduardo", "Maximiliano"]
print(Nombre_Familia)

Febrero= [30, 32, 31, 33, 28, 26, 30, 30, 28, 25, 32, 33, 36, 38, 40, 29, 33, 23, 26, 27, 33, 34, 35, 36, 33, 35, 37, 40]
print(Febrero)


Ciudades_Visitadas= ["Villa Carlos Paz", "Ciudad Autonoma de Buenos Aires", "La Cumbrecita", "Santa Rosa de Calamuchita", "Villa General Belgrano", "Rosario"]
print(Ciudades_Visitadas)

Eventos_Importantes=[ "07/10/2004", " Nacimiento de Tomas", "13/01/2010", "Nacimiento de Agus"]
print(Eventos_Importantes)

Nombre_Familia.sort()
print("Nombre de Familia Ordenado Alfabeticamente", Nombre_Familia)

Febrero.sort()
print("Temperatura de Febrero ascendente", Febrero)

Febrero.extend ([23, 25, 26, 26, 27, 28, 28, 29, 30, 30, 30, 31, 32, 32, 33])
print(Febrero)

Nombre_Familia.remove("Maria Ester")
Nombre_Familia.remove("Eduardo")
print(Nombre_Familia)

Ciudades_Visitadas.remove("Ciudad Autonoma de Buenos Aires")
Ciudades_Visitadas.remove("Rosario")
print(Ciudades_Visitadas)



Tupla_1= ("Azucar", 595, 1000, "Gramos")

Tupla_2= ("Sentadillas", 15, 5, "Kilogramos")

Tupla_3= ("Vacaciones", 46, "Dias Habiles")


Lista_ejercicio= [Tupla_1, Tupla_2, Tupla_3]

print(Lista_ejercicio)


DiccionarioFamiliar= {222222: "Tomas", 3333333: "Agustin", 4444444: "Carolina", 555555: "Maximiliano"}
print(DiccionarioFamiliar)

DiccionarioFamiliar[666666]= "Abuela Ester"
DiccionarioFamiliar[777777]= "Abuelo Eduardo"

print(DiccionarioFamiliar)

import random
numerostelefono = {}
for i in range(5):
    clave = f"persona{i + 1}"
    numero = "3" + "".join(str(random.randint(0, 7)) for i in range(6))
    numerostelefono[clave] = numero

print(numerostelefono)

