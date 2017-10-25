# parcialito n°3
# /* class nodo --> value
#               --> sig
#
# /*lista_enlazada --->primero 

def insertar(self,value):
    _nodo = Nodo(value)
  
	#caso border
	if not self.primero:
		self.primero == _nodo
    	return None
  
  	#caso border
  	if not self.primero.sig:
    	if value >= self.primero.value:
      		self.primero.sig = _nodo
			return None
     
    	_nodo.sig = self.primero
    	self.primero = _nodo
		return None
	
	if not (value >= self.primero.value):
		_nodo.sig = self.primero
    	self.primero = _nodo
		return None
	
    previo = self.primero
    actual = self.primero.sig
    
    while actual.sig:
		if not ( actual.value >= value):
			_node.sig = actual
			previo.sig = _node
			return None
		
		previo = actual
		actual = actual.sig
	
	actual.sig = _nodo
	return
      
  
