
#Ejercicio 4: Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 400.60 pesos la hora, si lo hace en el turno diurno cobra 350.50 pesos la hora.  

hrs=int(input("Ingrese cuantas horas trabajo: "))
turno=int(input("Ingrese 1 para turno diurno y 2 para turno nocturno. "))
if turno==1:
    print(f"El sueldo del empleado sera de {hrs*350.50}")
elif turno==2:
    print(f"El sueldo del empleado sera de {hrs*400.60}")
else:
    print("El numero de turno que ingreso es incorrecto. Pruebe de nuevo")