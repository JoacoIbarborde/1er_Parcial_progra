
def funcion_cargar_matriz_notas(cantidad_alumnos, cantidad_examenes):
    """
    Carga una matriz de notas de alumnos verificando que las notas esten entre 1 y 10
    Parametros:
        cantidad_alumnos: Cantidad de alumnos ingresado por el profesor
        cantidad_examenes: Cantidad de exámenes ingresado por el profesor
    Retorna la matriz de notas con las notas ingresadas por el profesor
    """
    matriz_notas = [[0 for c in range(cantidad_examenes)] for f in range(cantidad_alumnos)] # Generamos la matriz con los datos ingresados con un 0 en cada indice
    
    for i in range(cantidad_alumnos):
        for j in range(cantidad_examenes):
            while True:
                nota = input(f"Ingresa la nota del alumno {i + 1} en el examen {j + 1} (entre 1 y 10): ") # Recorre la matriz y le pide al profesor que ingrese las notas de cada alumno y examen
                if nota.isdigit(): # Verifica que la notaingresada sea un numero entero
                    nota = int(nota)
                    if 1 <= nota <= 10: # Verifica que la nota ingresada sea un numero entre 1 y 10
                        matriz_notas[i][j] = nota  # Guarda la nota en la matriz
                        break
                    else:
                        print("La nota debe estar entre 1 y 10. Intente nuevamente")
                        
    print("\nBoletin:")
    for fila in matriz_notas:
        for nota in fila:
            print(f"{nota:3}", end=" ")
        print()

    return matriz_notas  # Retorna la matriz de notas con las notas ingresadas por el profesor

#funcion_cargar_matriz_notas(3,2)

def funcion_porcentaje_aprobados(matriz_notas):
    """
    Calcula el porcentaje de examenes aprobados de cada alumno y lo muestra en pantalla
    Parametros:
        matriz_notas: Matriz de las notas de los alumnios
    """
    for i in range(len(matriz_notas)):
        contador_aprobados = 0 # Contador de las notas aprobadas de cada alumno, este se genera cada vez que recorremos una fila
        for j in range(len(matriz_notas[i])): # Recorremos cada columna de la matriz manteniendo la fila que seria el alumno
            if matriz_notas[i][j] >= 6:
                contador_aprobados += 1 # Sumamos 1 al contador si la nota es 6 o mas
        porcentaje_aprobados = (contador_aprobados / len(matriz_notas[i])) * 100 # Calculamos el porcentaje de aprobado de cada alumnio
        print(f"El alumno {i + 1} aprobó el{porcentaje_aprobados:.2f}% de los parciales")
    return


# Probando el parcial :)
funcion_porcentaje_aprobados(funcion_cargar_matriz_notas(4,3))
