# Las pilas se usan usualmente
# /* invertir listas de datos
# /* notacion polaca inversa
# /* recursividad


class PILA:
	"""TDA
		Primitivas
		/* constructor
		/* apilar <- value
		/* desapilar -> value
		/* ver_ultimo -> value
		/* esta_vacia -> bool
		/* tamaño -> len
	"""
	
	def __init__(self):
		self.contenedor = []
	
	def desapilar(self):
		if self.esta_vacia():
			return None
		
		return self.contenedor.pop()
	
	def apilar(self,value):
		self.contenedor.append(value)
	
	def esta_vacia(self):
		return self.tamanio == 0
	
	def ver_ultimo(self):
		if self.esta_vacia:
			return None
		
		return self.contenedor[-1]
	
	def tamanio(self):
		return len(self.contenedor)
		
