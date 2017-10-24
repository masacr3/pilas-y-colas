class Nodo:
	def __init__(self,value):
		self.value = value
		self.sig = None
	
	def __str__(self):
		return str(self.value)

class ListaEnlazada:
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.len = 0
	
	def push(self,value):
		_nodo = Nodo(value)
		self.len += 1
		
		if not self.primero:
			self.primero = self.ultimo = _nodo
			return None
		
		#apunto al nodo
		self.ultimo.sig = _nodo
		
		#me posiciono en el ultimo nodo
		self.ultimo = _nodo
	
	def pop(self):
		if not self.primero:
			return None
		
		if self.primero == self.ultimo:
			self.len -= 1
			value = self.primero.value
			self.primero = self.ultimo = None
			return None
		
		previo = self.primero
		actual = self.primero.sig
		
		while not (actual == self.ultimo):
			previo = actual
			actual = actual.sig
		
		self.ultimo = previo
		self.ultimo.sig = None
		
		return actual.value
		
		
		
		
		
		
