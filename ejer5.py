#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 5: Ingresar por teclado las edades de 3 participantes de un concurso. Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado. 

min=int(input("Ingrese la edad minima para el concurso: "))
part1=int(input("Ingrese la edad del primer participante: "))
part2=int(input("Ingrese la edad del segundo participante: "))
part3=int(input("Ingrese la edad del tercer participante: "))

if part1<min or part2<min or part3<min:
    print("El concurso no se puede llevar a cabo ya que no todos cumplen con la edad minima")
else:
    print("Todos cumplen con la edad minima")