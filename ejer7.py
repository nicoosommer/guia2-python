#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 7: Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un día y determinar cuál es el promedio de las temperaturas y si existe alguna temperatura que sea mayor al promedio. 
temp1=float(input("Ingrese la temperatura 1: "))
temp2=float(input("Ingrese la temperatura 2: "))
temp3=float(input("Ingrese la temperatura 3: "))
prom=(temp1+temp2+temp3)/3
print(f"El promedio es de {prom}")
if temp1>prom:
    print(f"La temperatura 1 ({temp1}) es mayor al promedio.")
if temp2>prom:
    print(f"La temperatura 2 ({temp2}) es mayor al promedio.")
if temp3>prom:
    print(f"La temperatura 3 ({temp3}) es mayor al promedio.")