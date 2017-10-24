# / invierte una lista mediante TDA pila
lista = [1,2,3,4,5]

mipila = PILA()

for n in lista:
	mipila.apila(n)

for i in range(mipila.tamanio()):
	print(mipila.desapila())


