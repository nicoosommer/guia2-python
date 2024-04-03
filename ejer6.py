#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 6: Una persona compra un billete de Quiniela y apuesta 3 números a la cabeza. En el caso que acierte alguno de ellos ganará 70 veces el monto de lo apostado. Crear un programa que genere un número al azar del 0 al 99 y que permita apostar los tres valores. En el caso que se acierte indicar el monto a cobrar. 

import random
quini1=random.randrange(0,99)
quini2=random.randrange(0,99)
quini3=random.randrange(0,99)
apuesta=int(input("Ingrese cuanto quiere apostar: "))
num1=int(input("Ingrese el primer num entre 0 y 99: "))
num2=int(input("Ingrese el segundo num entre 0 y 99: "))
num3=int(input("Ingrese el tercer num entre 0 y 99: "))
if num1==quini1 or num1==quini2 or num1==quini3:
    if num2==quini1 or num2==quini2 or num2==quini3:
        if num3==quini1 or num3==quini2 or num3==quini3:
            print(f"Acaba de ganar {apuesta*70}! Felicitaciones")
else:
    print(f"Perdio. Los numeros correctos eran {quini1}, {quini2} y {quini3}")