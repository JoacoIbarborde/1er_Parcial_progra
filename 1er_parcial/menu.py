from funciones import *

def menu():
    """
    Muestra el menu de opciones y permite elegir al profesor una opcion para realizar.
    Retorna la opcion elegida poor el profesor
    """
    continuar_menu = "si"
    while continuar_menu.lower() == "si": # While para que se repita el menu hasta que el profesor lo desee
        print("Seleccione una opcion (primero cargue las notas): ")
        print("1. Cargar notas")
        print("2. Mostrar el porcentaje de aprobacion de cada alumno")
        print("3. Mostrar el alumno con mejor promedio")
        print("4. Buscar una nota en la lista completa de alumnos")
        opcion_seleccionada = input("Ingrese el numero de la opcion: ")
        match opcion_seleccionada:
            case "1":  # Cada opcion que eliga el profesor se muestra en la terminal
                cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
                cantidad_examenes = int(input("ingrese la cantidad de examenes: "))
                notas_alumnos = cargar_matriz_notas(cantidad_alumnos, cantidad_examenes)
                otra_opcion = input("Desea elegir otra opcion? (si/no) ")
            case "2":
                porcentaje_aprobados(notas_alumnos)
                otra_opcion = input("Desea elegir otra opcion? (si/no) ")
            case "3":
                mejor_promedio(notas_alumnos)
                otra_opcion = input("Desea elegir otra opcion? (si/no) ")
            case "4":
                buscar_nota(notas_alumnos)
                otra_opcion = input("Desea elegir otra opcion? (si/no) ")
            case _:
                print("Opcion no valida. Intente nuevamente")
    else:
        return