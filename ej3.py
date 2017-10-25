# TDA pila
# con todas sus primitivas
# /* parcialito 3 

def esta_(cola,elemento):
	if cola.esta_vacia():
		return False
	
	esta = False
	_cola = Cola()
	
	while not cola.esta_vacia():
		value = cola.desenconlar()
		if value == elemento:
			esta = True
		
		_cola.encolar(value)
		
		if esta:
			continue
			
	while not _cola.esta_vacia():
		cola.encolar(_cola.desencolar())
	
	return esta
		
	
