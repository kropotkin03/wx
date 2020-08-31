archivo = open("empleados.csv")
enca = archivo.readline()
print "Encabezado: ", enca
for linea in archivo:
    print linea
archivo.close()