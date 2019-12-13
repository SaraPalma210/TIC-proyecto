#!
#-*- coding:utf-8 -*-
import sys
import zipfile
import os
import getpass
def readsize():
	size=int(input("\nIntroduzca el tamaño en byte a partir del cual depuraremos: "))
	return size

#asegurarse de que Google Chrome está cerrado

opcion=0
while (opcion!=5):
	print("1.- Mostrar archivos seleccionados")

	print("2.- Borrar archivos seleccionados")

	print("3.- Comprimir ficheros")

	print("4.- Borrar caché")

	print("5.- Salir")

	opcion = int(input("Seleccione una opción (1-5):"))
	if (opcion==1):
		lista02=[]
		size=readsize()
		ruta= input("\n¿Ubicación de la ruta-carpeta? ")
		os.chdir(ruta)
		lista01=os.listdir(".")
		for file in lista01:
			filesize=int(os.stat(file).st_size)
			if filesize>=size:
				indice=lista01.index(file)
				lista02.append(lista01[indice])
			else:
				pass
		print(lista02)

	elif (opcion==2):
		size=readsize()
		ruta= input("\n¿Ubicación de la ruta-carpeta? ")
		os.chdir(ruta)
		
		c=0
		while c==0:
			lista03=[]
			listado=os.listdir(".")
			for file in listado:
				filesize=int(os.stat(file).st_size)
				if filesize>=size:
					indice=listado.index(file)
					lista03.append(listado[indice])
				else:
					pass
	
			print(lista03)
			ficheroborrable= input("Introduzca nombre del fichero o escriba todos según desee borrar: ")
			ficheroborrable=ficheroborrable.lower()
			if ficheroborrable=="todos":
				for file in lista03:
					os.remove(file)
				print("Todos los ficheros del directorio de tamaño superior han sido borrados correctamente")
			else:
				os.remove(ficheroborrable)
				print("Fichero eliminado correctamente")
			d=input("¿Desea seguir borrando ficheros S/N?")
			d = d.lower()
			if (d=="n"):
				c=c+1
			else:
				pass

	elif (opcion==3):
		ruta= input("\n¿Qué desea comprimir? ")
		lista = os.listdir(ruta)
		print(lista)
		zip = zipfile.ZipFile('comprimido.zip', 'w')
		zip.write(ruta+"\\", compress_type=zipfile.ZIP_DEFLATED)
		zip.close()

	elif (opcion==4):
		a = input("¿Tiene el navegador abierto? S/N: ")
		a = a.lower()
		if a=="s":
			print("Asegúrese de tener el navegador cerrado")
		else:
			usuario = getpass.getuser()
			n = "C:\\Users\\" + usuario + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
			os.chdir(n)
			chrome = os.listdir(".")
			for file in chrome:
				os.remove(file)
			print("Ejecución completada")
	elif (opcion==5):
		sys.exit()
	else:
		print("Opción no disponible")
