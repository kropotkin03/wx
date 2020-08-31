# -*- coding:utf-8 -*-
print "Con with"
with open("alumnos-python.csv", "r+") as foooo:
    for linea in foooo:
        print linea
print "Fin with"

print "read completo"
archivo = open("alumnos-python.csv")
print archivo
contenido = archivo.read()
print contenido
print "FIN read completo"

print "con FOR"
archivo = open("alumnos-python.csv")
for linea in archivo:
    print linea
print "fin con FOR"

print "lectura parcial"
archivo = open("alumnos-python.csv")
doscientos = archivo.read(200)
print doscientos
veinte = archivo.read(20)
print veinte
dos = archivo.read(2)
print dos
archivo.close()
print "fin lectura parcial"

print "grabar"
nuevo = open("nuevo.txt", "w")
lista = ["juan", "ana", "luis"]
for nombre in lista:
    nombre = nombre + "\n"
    nuevo.write(nombre)
nuevo.close()

hola = open("hola.txt", "w")
lineas_de_texto = ["una línea de texto\n", "otra línea de texto\n", "y una tercera\n"]
hola.writelines(lineas_de_texto)
hola.close()

print "agregar"
nuevo_pero_mas_largo = open("nuevo.txt", "a")
nuevo_pero_mas_largo.write("cuarta línea agregada")
nuevo_pero_mas_largo.close()
