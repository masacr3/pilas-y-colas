class PILA:
	"TDA"
	
	def __init__(self):
		self.contenedor = []
	
	def pop(self):
		if self.vacia():
			return None
		
		return self.contenedor.pop()
