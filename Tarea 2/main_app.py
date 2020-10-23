from programaFinanzas import Ingresos, Egresos, Finanzas

Finanzas = Finanzas()

while True:
    print("-" * 60)
    print("Ingrese el número de la operación que desee realizar: ")
    print("0-Salir del programa")
    print("1-Registrar un ingreso")
    print("2-Registrar un egreso")
    print("3-Ver el reporte de ingresos")
    print("4-Ver el reporte de egresos")
    print("5-Ver el reporte de transacciones")
    print("6-Ver el total en la cuenta")
    opcion = int(input("Opción: "))
    print("-" * 60)

    if opcion == 0:
        print("Gracias por utilizar el programa de finanzas")
        break
    if opcion == 1:
        ingreso = float(input("Ingresos a registrar: $"))
        Finanzas.regIngresos(Ingresos(ingreso))
    if opcion == 2:
        egreso = float(input("Egresos a registrar: $"))
        Finanzas.regEgresos(Egresos(egreso))
    if opcion == 3:
        Finanzas.reporteIngresos()
    if opcion == 4:
        Finanzas.reporteEgresos()
    if opcion == 5:
        Finanzas.reporteTransacciones()
    if opcion == 6:
        Finanzas.imprimeTotales()
