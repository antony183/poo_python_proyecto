# Clase derivada Estudiante
# Aplica herencia y polimorfismo

from .persona import Persona   # 👈 IMPORT CORRECTO

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Método sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.get_nombre()}, estudio {self.carrera} y tengo {self.get_edad()} años."
