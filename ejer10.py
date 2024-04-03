#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 10: El IMC es el índice de masa corporal de una persona y se calcula haciendo el cociente entre su peso en kg y su altura en metros al cuadrado. Si el índice es mayor a 30 se encuentra en un grado de obesidad. Si el índice se encuentra entre  24.5 y 29.9 se encuentra en sobrepeso. Si el índice se encuentra entre  18.5 y 24.9 se encuentra en un peso saludable. Si el índice se encuentra inferior a  18.5 se encuentra en un peso insuficiente. Realizar un programa que permita calcular el IMC de una persona y le indique en qué condición se encuentra y además le indique cuál sería su peso ideal para su altura. Nota: se toma como referencia un IMC de 21.7 como ideal.

peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en metros: "))
imc=peso/(altura**2)
if imc>30:
    estado="obesidad"
elif imc>=24.5:
    estado="sobrepeso"
elif imc>=18.5:
    estado="peso saludable"
else:
    estado="peso insuficiente"
print(f"Su imc es de {imc} y se encuentra en un estado de {estado}. Su peso ideal seria de {21.7*(altura**2)}")
