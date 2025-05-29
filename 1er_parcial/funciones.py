
def cargar_matriz_notas(cantidad_alumnos, cantidad_examenes):
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

#cargar_matriz_notas(3,2)

def porcentaje_aprobados(matriz_notas):
    """
    Calcula el porcentaje de examenes aprobados de cada alumno y lo muestra en pantalla
    Parametros:
        matriz_notas: Matriz de las notas de los alumnos
    """
    for i in range(len(matriz_notas)):
        contador_aprobados = 0 # Contador de las notas aprobadas de cada alumno, este se genera cada vez que recorremos una fila
        for j in range(len(matriz_notas[i])): # Recorremos cada columna de la matriz manteniendo la fila que seria el alumno
            if matriz_notas[i][j] >= 6:
                contador_aprobados += 1 # Sumamos 1 al contador si la nota es 6 o mas
        porcentaje_aprobados = (contador_aprobados / len(matriz_notas[i])) * 100 # Calculamos el porcentaje de aprobado de cada alumno
        print(f"El alumno {i + 1} aprobó el {porcentaje_aprobados:.2f}% de los parciales ")
    return

# Probando el parcial :)
#porcentaje_aprobados(cargar_matriz_notas(4,3))

def mejor_promedio(matriz_notas):
    """
    Calcula el promedio de cada amigo y determina cual tiene el mejor promedio entre todos los alumnos.
    Parametos:
        matriz_notas: Matriz de las notas de los alumnos
    Retorna el indice del alumno y el valor del promedio
    """
    mejor_promedio = float("-inf") # Creo un valor infinito negativo para tener un valor inicial para la comparacion
    alumno_mejor_promedio = 0  # -1 para no tener errores al momento de sumarle el indice
    
    for i in range(len(matriz_notas)):
        acumulador_notas_alumno = 0 # acumulador para las notas de cada alumno
        for j in range(len(matriz_notas[i])):
            acumulador_notas_alumno += matriz_notas[i][j] # sumo cada nota del alumno al acumulador
        promedio_alumno = (acumulador_notas_alumno / len(matriz_notas[i])) # Hago el promedio de cada alumno
        
        if promedio_alumno > mejor_promedio:  # Comparacion entre los promedios para ver cual alumno tiene el mas alto
            mejor_promedio = promedio_alumno # reemplaza el ultimo mayor promedio por el mas alto si es que hay uno
            alumno_mejor_promedio = i + 1 # me llevo el indice de cada alumno para poder mostrarlo
            
    print(f"El alumno con mejor promedio es el alumno {alumno_mejor_promedio} con un promedio de {mejor_promedio}")
    return alumno_mejor_promedio, promedio_alumno

#mejor_promedio(cargar_matriz_notas(4,3))

def buscar_nota(matriz_notas):
    """
    Retorna una lista con todas las posiciones de la matriaz donde aparece la nota que pida el profesor
    Parametros:
        Matriz_notas: matriz de las notas de los alumnos
    """
    lista_nota_buscada = [] # genero una lista vacia para poder guardar la posicion de las notas encontradas
    
    nota_buscada = int(input("Cual es la nota que desea buscar? "))
    if nota_buscada >= 1 and nota_buscada <= 10: # validacion de las notas
        for i in range(len(matriz_notas)): 
            for j in range(len(matriz_notas[i])): # recorro la lista
                if nota_buscada == matriz_notas[i][j]:   
                    lista_nota_buscada.append((i + 1, j + 1)) # Si la nota buscada se encuentra en la lista, agrega la posicion a la lista.
        
        if lista_nota_buscada: # booleano para mostrar la lista  si es que se encuentra la nota
            print(f"La nota buscada se encuentra en las posiciones: ")
            print(lista_nota_buscada)
        else: 
            print("La nota buscada no pudo ser encontrada. Intente nuevamente") # si no se encuentra retorna mensaje de error
    else:
        print("La nota debe estar entre 1 y 10. Intente nuevamente")

    return lista_nota_buscada

#buscar_nota(cargar_matriz_notas(4,3))
