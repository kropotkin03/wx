class Telefono():
    marca = ""
    modelo = ""
    costo = 0
    def costo_anual(self, c):

        return c * 12

t1 = Telefono()
t1.costo = 120
t1.costo_anual(t1.costo)
