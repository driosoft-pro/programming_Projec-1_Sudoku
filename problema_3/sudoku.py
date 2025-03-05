import os  # Importa la librería os para interactuar con el sistema operativo
import random  # Importa la librería random para generar números aleatorios

def limpiar_pantalla():
    """Limpia la pantalla en diferentes sistemas operativos."""
    os.system("cls" if os.name == "nt" else "clear")  # Limpia la pantalla según el sistema operativo

def mostrar_titulo():
    """Muestra el título del juego."""
    print("=" * 75)  # Imprime una línea de separación
    print(" " * 30, "JUEGO DE SUDOKU")  # Imprime el título del juego centrado
    print("=" * 75)  # Imprime otra línea de separación

def mostrar_reglas():
    # Función para mostrar las reglas del juego Sudoku en la consola
    print("=" * 75)  # Imprime una línea de separación
    print(" " * 28, "REGLAS DEL SUDOKU")  # Imprime un encabezado de las reglas con salto de línea inicial
    print("=" * 75)  # Imprime otra línea de separación
    print("1. Se genera un tablero de Sudoku 9x9 con algunos espacios vacíos.")  # Explica la primera regla
    print("2. Debes rellenar los espacios vacíos con números del 1 al 9.")  # Explica la segunda regla
    print("3. No puedes repetir números en la misma fila, columna o subcuadrícula 3x3.")  # Explica la tercera regla
    print("4. Ganas cuando completas el tablero correctamente.")  # Explica la cuarta regla
    print("5. Guia de ingreso de datos C para columnas y F para Filas")  # Explica la quinta regla
    print("=" * 75)  # Imprime una línea divisoria para finalizar la sección de reglas

def imprimir_tablero(tablero):
    """Imprime el tablero de Sudoku con formato estructurado."""
    print("\n  C 0 1 2 | 3 4 5 | 6 7 8")  # Imprime el encabezado de las columnas
    print("F ┌-----------------------┐")  # Imprime la parte superior del tablero

    for fila in range(9):  # Itera sobre cada fila del tablero
        if fila in [3, 6]:  # Imprime un separador horizontal cada 3 filas
            print("  |-------|-------|-------|")  # Separador de bloques

        print(f"{fila} |", end=" ")  # Imprime el número de la fila y el borde izquierdo del tablero
        for col in range(9):  # Itera sobre cada columna de la fila
            if col in [3, 6]:  # Imprime un separador vertical cada 3 columnas
                print("|", end=" ")  # Separador vertical de bloques

            print(tablero[fila][col] if tablero[fila][col] != 0 else ".", end=" ")  # Imprime el número o un punto si la celda está vacía

        print("|")  # Imprime el borde derecho del tablero

    print("  └-----------------------┘")  # Imprime la parte inferior del tablero

def generar_subtablero(tablero, fila, col, num):
    """Verifica si un número puede colocarse en la posición dada."""
    if num in tablero[fila]:  # Verifica si el número ya está en la fila
        return False

    for i in range(9):  # Verifica si el número ya está en la columna
        if tablero[i][col] == num:
            return False

    inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3  # Calcula el inicio de la subcuadrícula 3x3
    for i in range(3):  # Itera sobre las filas de la subcuadrícula
        for j in range(3):  # Itera sobre las columnas de la subcuadrícula
            if tablero[inicio_fila + i][inicio_col + j] == num:  # Verifica si el número ya está en la subcuadrícula
                return False

    return True  # Retorna True si el número puede colocarse en la posición dada

def generar_tablero(tablero):
    """Verifica si el tablero está lleno."""
    for fila in tablero:  # Itera sobre cada fila del tablero
        if 0 in fila:  # Verifica si hay alguna celda vacía (con valor 0)
            return False
    return True  # Retorna True si el tablero está lleno

def generar_sudoku():
    """Genera un Sudoku completo válido."""
    def resolver_sudoku(tablero):
        """Resuelve el Sudoku con backtracking."""
        for fila in range(9):  # Itera sobre cada fila del tablero
            for col in range(9):  # Itera sobre cada columna de la fila
                if tablero[fila][col] == 0:  # Verifica si la celda está vacía
                    for num in range(1, 10):  # Intenta colocar números del 1 al 9
                        if generar_subtablero(tablero, fila, col, num):  # Verifica si el número puede colocarse
                            tablero[fila][col] = num  # Coloca el número en la celda
                            if resolver_sudoku(tablero):  # Llama recursivamente para resolver el resto del tablero
                                return True
                            tablero[fila][col] = 0  # Si no se puede resolver, vacía la celda y prueba con otro número
                    return False  # Retorna False si no se puede colocar ningún número en la celda
        return True  # Retorna True si el tablero está resuelto

    tablero = [[0 for _ in range(9)] for _ in range(9)]  # Inicializa un tablero vacío (9x9) con ceros
    resolver_sudoku(tablero)  # Llama a la función para resolver el Sudoku
    return tablero  # Retorna el tablero resuelto

def eliminar_numeros(tablero, porcentaje):
    """Elimina números del tablero según la dificultad."""
    num_casillas_a_vaciar = int(81 * porcentaje)  # Calcula el número de celdas a vaciar según el porcentaje
    casillas = [(fila, col) for fila in range(9) for col in range(9)]  # Crea una lista con todas las posiciones del tablero
    random.shuffle(casillas)  # Mezcla aleatoriamente las posiciones

    for _ in range(num_casillas_a_vaciar):  # Itera sobre el número de celdas a vaciar
        fila, col = casillas.pop()  # Toma una posición aleatoria de la lista
        tablero[fila][col] = 0  # Vacía la celda en la posición seleccionada

def generar_dificultad():
    """Permite seleccionar la dificultad."""
    niveles = {
        "1": ("Súper fácil", 3/81),  # Define el nivel "Súper fácil" con su porcentaje de celdas vacías
        "2": ("Fácil", 0.30),  # Define el nivel "Fácil" con su porcentaje de celdas vacías
        "3": ("Medio", 0.45),  # Define el nivel "Medio" con su porcentaje de celdas vacías
        "4": ("Difícil", 0.70)  # Define el nivel "Difícil" con su porcentaje de celdas vacías
    }

    print("\nSelecciona la dificultad:")  # Imprime el mensaje para seleccionar la dificultad
    for clave, (nombre, _) in niveles.items():  # Itera sobre los niveles de dificultad
        print(f"{clave}. {nombre}")  # Imprime cada nivel de dificultad con su clave

    while True:  # Bucle infinito para solicitar una opción válida
        opcion = input("Opción: ")  # Solicita la opción al usuario
        if opcion in niveles:  # Verifica si la opción es válida
            return niveles[opcion][1]  # Retorna el porcentaje correspondiente al nivel seleccionado
        print("Opción no válida, intenta nuevamente.")  # Imprime un mensaje de error si la opción no es válida

def obtener_dificultad(mensaje, min_val, max_val):
    """Solicita un número al usuario y maneja errores."""
    while True:  # Bucle infinito para solicitar un número válido
        try:
            num = int(input(mensaje))  # Solicita el número al usuario y lo convierte a entero
            if min_val <= num <= max_val:  # Verifica si el número está dentro del rango permitido
                return num  # Retorna el número si es válido
            print(f"Error: Ingresa un número entre {min_val} y {max_val}.")  # Imprime un mensaje de error si el número está fuera del rango
        except ValueError:
            print("Error: Debes ingresar un número válido.")  # Imprime un mensaje de error si la entrada no es un número válido

def jugar_sudoku():
    """Función principal para jugar Sudoku."""
    limpiar_pantalla()  # Limpia la pantalla
    mostrar_titulo()  # Muestra el título del juego

    tablero = generar_sudoku()  # Genera un tablero de Sudoku completo
    porcentaje_vacio = generar_dificultad()  # Solicita al usuario seleccionar la dificultad
    eliminar_numeros(tablero, porcentaje_vacio)  # Elimina números del tablero según la dificultad seleccionada

    while not generar_tablero(tablero):  # Bucle que se ejecuta mientras el tablero no esté lleno
        limpiar_pantalla()  # Limpia la pantalla
        mostrar_reglas()  # Muestra las reglas del juego
        mostrar_titulo()  # Muestra el título del juego
        imprimir_tablero(tablero)  # Imprime el tablero actual

        print("\nIngrese las coordenadas y el número a colocar:")  # Solicita al usuario ingresar las coordenadas y el número

        fila = obtener_dificultad("Ingresa la fila (0-8): ", 0, 8)  # Solicita la fila al usuario
        col = obtener_dificultad("Ingresa la columna (0-8): ", 0, 8)  # Solicita la columna al usuario

        if tablero[fila][col] != 0:  # Verifica si la celda ya tiene un número
            print("Error: La celda ya tiene un número. Intenta en otra posición.")  # Imprime un mensaje de error
            continue  # Continúa con la siguiente iteración del bucle

        num = obtener_dificultad("Ingresa un número (1-9): ", 1, 9)  # Solicita el número al usuario

        if generar_subtablero(tablero, fila, col, num):  # Verifica si el número puede colocarse en la posición dada
            tablero[fila][col] = num  # Coloca el número en la celda
        else:
            print("Error: Número no válido en esta posición. Intenta de nuevo.")  # Imprime un mensaje de error

    limpiar_pantalla()  # Limpia la pantalla
    mostrar_titulo()  # Muestra el título del juego
    imprimir_tablero(tablero)  # Imprime el tablero completo
    print("\n¡Felicidades! Has completado el Sudoku correctamente.")  # Imprime un mensaje de felicitación

def main():
    jugar_sudoku()  # Llama a la función principal para jugar Sudoku

if __name__ == "__main__":
    main()  # Ejecuta la función main si el script se ejecuta directamente