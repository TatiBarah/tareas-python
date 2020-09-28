listaRegistro = []
respuesta = ""
costoTotal = 0.0
print("Puedes comenzar a agregar a los clientes:")
while respuesta != "No":
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = input("Costo ($0.00): ")
    costo = float(costo)
    registro = {"cliente": cliente, "producto": producto, "costo": costo}
    listaRegistro.append(registro)
    costoTotal += costo
    print("")
    print("El costo total de los productos registrados es: $" + str(costoTotal))
    print("")
    respuesta = input("¿Deseas seguir agregando clientes? (Sí o No): ")
    print("")

print("Los registros son:")
for registro in listaRegistro:
    print(registro)
print("El costo total es $" + str(costoTotal))
