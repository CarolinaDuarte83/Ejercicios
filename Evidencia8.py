# '''Ejercicios Estructuras Condicionales:
# Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea
# correspondiente:'''
# #1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo!

# #2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco, seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

Numero= int(input ("Ingrese un numero "))
if Numero == 10:
    print("¡Usted ha ganado el sorteo!")

elif Numero < 10:
    print("¡Falto un poco, seguí participando!")

else:
    print("¡Te pasaste, a seguir intentando!")


#3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.


Dia= input("Ingrese un dia de la semana ").lower()
if Dia == "lunes":
    print("Buen comienzo de Semana")
elif Dia == "viernes":
    print("Llego el ultimo dia de la semana")
elif Dia == "sabado" or Dia == "domingo":
    print("Llego el fin de semana!")        

else:
    print("Feliz semana!")


#4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.

Letra=input("Ingrese una letra ").lower()
if Letra in {"a", "e" , "i", "o", "u"}:
    print("Es vocal")


else:
    print(" Usted NO selecciono una Vocal")




#1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar hasta que se ingrese -1

Sumatoria = 0 

while True: 
    numero = float(input(" Ingrese los numeros que desea sumar,para finalizar debera ingresar -1 \n" ))
    if numero== -1:
        break
    Sumatoria += numero

print (f"La suma total es {Sumatoria}")



#2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.


cantidad_numeros = int (input ("Ingrese la cantidad de numeros que desee \n"))

mayor_a_cero= 0

menor_a_cero= 0

igual_a_cero= 0 

for i in range (cantidad_numeros):

     numeros_introducidos= float (input ("Introduzca los numeros que va a ingresar \n"))
     mayor_a_cero += numeros_introducidos > 0
     menor_a_cero += numeros_introducidos < 0
     igual_a_cero += numeros_introducidos== 0 

print(f"Cantidad de numeros mayores a 0 es {mayor_a_cero} , Cantidad de numeros menores a 0 es {menor_a_cero} , Cantidad de numeros igual a 0 es {igual_a_cero}" )




#3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un cero.

while True: 

    Letra= input("Ingrese una letra, si desea finalizar presione 0 ").lower()
    if Letra == "0":
        print("Ha finalizado el programa ")
        break

    elif Letra in {"a", "e" , "i", "o", "u"}:
        print(" VOCAL ")
    
    else:
        print (" NO VOCAL ")    



#4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.    


Cantidad_Numeros= 0

Suma_Numeros= 0


while True:
    Introducir_Numeros = int(input ("Ingrese los numeros que desee, para finalizar introduzca 0 "))

    if Introducir_Numeros == 0:
        print(" Ha finalizado la suma ")
        break

    Suma_Numeros += Introducir_Numeros
    Cantidad_Numeros += 1
    Media_Numeros= Suma_Numeros/Cantidad_Numeros
print(f"La suma de los numeros es {Suma_Numeros}, La media de los numeros es {Media_Numeros}")


