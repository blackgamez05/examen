#EJERCICIO PARA GESTIONAR UNA LISTA DE CONTACTOS
import os
os.system("cls || clear")
#crear clase contacto
class contacto:
    def __init__(self,nombre,numero_telefono):
        self.nombre = nombre
        self.numero_telefono = numero_telefono
    def contactar(self):
        print (f"este contacto es{self.nombre}y su numero de telefono es: {self.numero_telefono}")
#seleccionar el contacto que desee
contacto1 = contacto ("carlos", 83827052)
contacto2= contacto ("jose", 83349738)
contacto3= contacto ("josue", 85882413)
contacto1.contactar()