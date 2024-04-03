#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 3: Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2, en caso contrario elevar el resultado al cubo. 

num1=int(input("Ingrese el num1: "))
num2=int(input("Ingrese el num2: "))
num3=int(input("Ingrese el num3: "))
sum=num1+num2+num3
if sum>10:
    sum=sum/2
else:
    sum=sum**3
print(f"El resultado final es {sum}")