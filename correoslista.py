#!/usr/bin/python
# -*- coding: utf -8-*-

#paso 1: almacenar nuestros datos
nombres=[
	["Alejandra Campos", "aedith_school@gmail.com"],
	["Enique Cortez", "pirataenrique@yahoo.com"],
	["Shantal Delfin", "shantal27@hotmail.com"],
	["Leonardo Suarez", "leosuarez@hotmail.com"],
	["Rafael Contreras", "ralph_vp@hotmail.com"],
]

#paso 2: Imprimir nombres en nombre alfabetico con nombre y e-mail
#ordenamos la lista con la instruccion .sort()
nombres.sort()
for nom in nombres:
	print (nom)

#paso 3: imprimir nombre indicando cuentas letras tiene cada nombre
print()
print("EL TOTAL DE LETRAS ES:")
print()
for letra in nombres:
	caracteres = len(letra[0])-1
	print (letra[0] + " " + str(caracteres))

#paso 4: imprimir el dominio de los email

print()
print("Dominios")
print()
for nom in nombres:
	dominio=nom[1].split ("@")[1]
	print(""+ dominio)

