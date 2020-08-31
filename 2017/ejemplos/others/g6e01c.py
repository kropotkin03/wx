class Telefono():
    marca = ""
    modelo = ""
    costo = 0

    def costo_anual(self):
        return self.costo * 12

t1 = Telefono()
t1.costo = 120
print t1.costo_anual()

