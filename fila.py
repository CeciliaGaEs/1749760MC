class fila:
	def _init_(self):
		self.fila=[]
	
	def obtener (self):
		return self.fila.pop()
	def meter (self,e):
		self.fila.append(e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)
l = fila()
l.meter(1)
l.meter(2)
l.meter(3)
print(l.longitud)
print(l.obtener())
