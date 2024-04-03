#
#Ejercicio 8: Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra, papel o Tijera” y determine cuál de ellos es el ganador.  Las reglas son:  * La piedra aplasta (o rompe) la Tijera. (Gana la piedra).  * La Tijera corta el papel. (Gana la Tijera). El papel envuelve la piedra. (Gana el papel)  * Si los dos jugadores eligen el mismo elemento, empatan.
import random
opciones=["piedra","papel","tijera"]
jugador=input("Ingrese piedra, papel o tijera: ").lower()
cpu = random.choice(opciones)
print("Opcion de la pc: ",cpu)
print("Opcion del jugador: ",jugador)
if cpu==jugador:
      print("Empate")
elif jugador=="piedra":
     if cpu=="tijera":
         print("El jugador gana")
     else:
        print("La maquina gana")
elif jugador=="papel":
    if cpu=="piedra":
        print("El jugador gana")
    else:
         print("La maquina gana")
elif jugador=="tijera":
    if cpu=="papel":
          print("El jugador gana")
    else:
         print("La maquina gana")