# Clase base Persona
# Aplica encapsulación y polimorfismo

class persona:
    def __init__(self, nombre, edad):
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método polimórfico
    def presentarse(self):
        return f"Hola, soy {self.__nombre} y tengo {self.__edad} años."
