class Ingresos:
    def __init__(self, total):
        self.total = total


class Egresos:
    def __init__(self, total):
        self.total = total


class Finanzas:
    saldoEnCuenta = 0.0
    listaIngresos = []
    listaEgresos = []
    listaTransacciones = []

    def regIngresos(self, totalRegistrado):
        self.saldoEnCuenta += totalRegistrado.total
        self.listaIngresos.append(totalRegistrado.total)
        self.listaTransacciones.append(totalRegistrado.total)

    def regEgresos(self, totalRegistrado):
        self.saldoEnCuenta -= totalRegistrado.total
        self.listaEgresos.append(totalRegistrado.total)
        self.listaTransacciones.append(totalRegistrado.total * -1)

    def reporteIngresos(self):
        print("Estos son todos tus ingresos:")
        ingresos = sum(self.listaIngresos)
        print(self.listaIngresos)
        print("Tus ingresos totales son: $" + str(ingresos))

    def reporteEgresos(self):
        print("Estos son todos tus egresos:")
        egresos = sum(self.listaEgresos)
        print(self.listaEgresos)
        print("Tus egresos totales suman: $" + str(egresos))

    def reporteTransacciones(self):
        print("Este es el reporte de todas las transacciones que realizaste: ")
        ingresos = 0.0
        egresos = 0.0
        print(self.listaTransacciones)
        for transaccion in self.listaTransacciones:
            if transaccion < 0:
                egresos += transaccion * -1
            else:
                ingresos += transaccion
        print("El total de tus ingresos es de: $" + str(ingresos))
        print("El total de tus egresos es de: $" + str(egresos))
        print("El total en tu cuenta es de: $" + str(self.saldoEnCuenta))

    def imprimeTotales(self):
        print("El total en tu cuenta es de: $" + str(self.saldoEnCuenta))