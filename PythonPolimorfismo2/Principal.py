from paquete.PersonaEquipo import *
f= Futbolista("Eduardo")
m=Medico("Maria")
p=Presidente("Pedro")
e=Entrenador("Kaviedes")

lista=[f,m,p,e]

for l in lista:
	l.entrenar()
