from paquete.PersonaEquipo import *
persona=PersonaEquipo()
persona.agregar_nombre("Ana")
print(persona.entrenar())
f=Futbolista()
f.agregar_nombre("Maria")
f.entrenar()

e=Entrenador()
e.entrenar()

lista = [persona, f, e]

for l in lista:
	l.entrenar()
