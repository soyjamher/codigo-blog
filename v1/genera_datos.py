from Persona import Persona

import csv
#import os

myData = []
myHead = ["dia","mes","anio","nombres","paterno","materno","sexo","curp","rfc"]


with open('datos_generados.csv', mode='w', newline='') as archivo_nombres:
    nombres_writer = csv.writer(archivo_nombres, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    nombres_writer.writerow(myHead)

#with open('datos_generados.csv', 'a') as the_file:
#	for item in myHead:
 #       the_file.write("%s\n" % item)
    #the_file.write(str(myHead))
nregistros = int(input("Dime cuantos nombres generar: "))
for x in range(nregistros):
	persona = Persona() 
	renglon = []
	renglon.append(persona.dd)
	renglon.append(persona.mm)
	renglon.append(persona.yyyy)
	renglon.append(persona.nombre)
	renglon.append(persona.paterno)
	renglon.append(persona.materno)
	renglon.append(persona.sexo)
	renglon.append(persona.curp)
	renglon.append(persona.rfc)
	myData.append(renglon)
print("Escribiendo archivo, espere por favor")
with open('datos_generados.csv', mode='a', newline='') as archivo_nombres:
    nombres_writer = csv.writer(archivo_nombres, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for item in myData:
    	nombres_writer.writerow(item)
#with myFile:
#    writer = csv.writer(myFile)
#    writer.writerows(myData)
print("archivo generado")