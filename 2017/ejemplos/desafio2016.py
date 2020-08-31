# coding=utf-8

"""
Una concesionaria de vehículos Ford tiene 4 modelos disponibles para la venta: Ka, Fiesta, Focus y Mondeo.
Cada modelo tiene un stock determinado.
Se reciben pedidos y a partir de allí se produce la siguiente secuencia:
Si tienen el modelo específico (y color?), se solicita la tarjeta de crédito y se cierra la operación,
si no lo tienen se da la opción de reserva (para pedido a fábrica) o bien cambio de modelo por otro
con stock. El cliente puede rechazar ambas opciones.

Se debe programar un test de 20 pedidos (con stock total < 20) y mostrar la salida.

"""

from wx import *

class MyApp(App):
    def OnInit(self):
        color = ["blanco", "negro", "rojo"]
        modelo = ["Ka", "Fiesta", "Focus", "Mondeo"]
        f = Frame(None)
        f.Show()


        return True

app = MyApp()
app.MainLoop()
