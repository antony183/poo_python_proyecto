# Archivo principal del programa

from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import GestorPersonas

def main():
    persona1 = Persona("Carlos", 40)
    estudiante1 = Estudiante("Ana", 20, "Administración de Empresas")
    estudiante2 = Estudiante("Luis", 22, "Ingeniería")

    gestor = GestorPersonas()
    gestor.agregar_persona(persona1)
    gestor.agregar_persona(estudiante1)
    gestor.agregar_persona(estudiante2)

    gestor.mostrar_presentaciones()

if __name__ == "__main__":
    main()
