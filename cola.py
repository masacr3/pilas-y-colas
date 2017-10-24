# Las colas se usan usualmente
# /* dar un orden de prioridad a los procesos
# /* listar cosas


class PILA:
	"""TDA
		Primitivas
		/* constructor
		/* encolar <- value
		/* desencolar -> value
		/* ver_primero -> value
		/* esta_vacia -> bool
		/* tamaño -> len
	"""
	
	def __init__(self):
		self.contenedor = []
	
	def desencolar(self):
		if self.esta_vacia():
			return None
		
		return self.contenedor.pop(0)
	
	def encolar(self,value):
		self.contenedor.append(value)
	
	def esta_vacia(self):
		return self.tamanio == 0
	
	def ver_primero(self):
		if self.esta_vacia:
			return None
		
		return self.contenedor[0]
	
	def tamanio(self):
		return len(self.contenedor)
