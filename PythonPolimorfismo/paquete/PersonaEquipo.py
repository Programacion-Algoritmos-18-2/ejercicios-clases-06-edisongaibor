class PersonaEquipo(object):
	def __init__(self):
		self.nombre = ""
	def agregar_nombre(self,nom):
		self.nombre = nom
	def obtener_nombre(self):
		return self.nombre
	def entrenar (self):
		print("Entreno")
class Futbolista(PersonaEquipo):
	def __init__(self):
		super(Futbolista, self).__init__()
		self.posicion_campo=""
	def agregar_posicion_campo(self,pos):
		self.posicion_campo = pos
	def obtener_posicion_campo(self):
		return self.posicion_campo
	def entrenar(self):
		print("Hago p en el entrenamiento")
class Entrenador(PersonaEquipo):
	def __init__(self):
		super(Entrenador,self).__init__()
		self.codigo_entrenador=""
	def agregar_codigo_entrenador(self,cod):
		self.codigo_entrenador = cod
	def obtener_codigo_entrenador(self):
		return self.codigo_entrenador


