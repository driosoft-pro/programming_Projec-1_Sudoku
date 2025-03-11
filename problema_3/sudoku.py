import os
import random

def limpiar_pantalla():
    """Limpia la pantalla en diferentes sistemas operativos."""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_titulo():
    """Muestra el título del juego."""
    print("=" * 75)
    print(" " * 30, "JUEGO DE SUDOKU")
    print("=" * 75)

def mostrar_reglas():
    """Muestra las reglas del juego Sudoku."""
    print("=" * 75)
    print(" " * 28, "REGLAS DEL SUDOKU")
    print("=" * 75)
    print("1. Se genera un tablero de Sudoku 9x9 con algunos espacios vacíos.")
    print("2. Debes rellenar los espacios vacíos con números del 1 al 9.")
    print("3. No puedes repetir números en la misma fila, columna o subcuadrícula 3x3.")
    print("4. Ganas cuando completas el tablero correctamente.")
    print("5. Guia de ingreso de datos C para columnas y F para Filas")
    print("=" * 75)

def imprimir_tablero(tablero):
    """Imprime el tablero de Sudoku con formato estructurado."""
    print("\n  C 0 1 2 | 3 4 5 | 6 7 8")
    print("F ┌-----------------------┐")

    for fila in range(9):
        if fila in [3, 6]:
            print("  |-------|-------|-------|")

        print(f"{fila} |", end=" ")
        for col in range(9):
            if col in [3, 6]:
                print("|", end=" ")

            print(tablero[fila][col] if tablero[fila][col] != 0 else ".", end=" ")

        print("|")

    print("  └-----------------------┘")

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

#def generar_tablero(tablero):
#    """Verifica si el tablero está lleno."""
#    for fila in tablero:  # Itera sobre cada fila del tablero
#        if 0 in fila:  # Verifica si hay alguna celda vacía (con valor 0)
#            return False
#    return True  # Retorna True si el tablero está lleno
#
#def generar_sudoku():
#    """Genera un Sudoku completo válido."""
#    def resolver_sudoku(tablero):
#        """Resuelve el Sudoku con backtracking."""
#        for fila in range(9):  # Itera sobre cada fila del tablero
#            for col in range(9):  # Itera sobre cada columna de la fila
#                if tablero[fila][col] == 0:  # Verifica si la celda está vacía
#                    for num in range(1, 10):  # Intenta colocar números del 1 al 9
#                        if generar_subtablero(tablero, fila, col, num):  # Verifica si el número puede colocarse
#                            tablero[fila][col] = num  # Coloca el número en la celda
#                            if resolver_sudoku(tablero):  # Llama recursivamente para resolver el resto del tablero
#                                return True
#                            tablero[fila][col] = 0  # Si no se puede resolver, vacía la celda y prueba con otro número
#                    return False  # Retorna False si no se puede colocar ningún número en la celda
#        return True  # Retorna True si el tablero está resuelto
#
#    tablero = [[0 for _ in range(9)] for _ in range(9)]  # Inicializa un tablero vacío (9x9) con ceros
#    resolver_sudoku(tablero)  # Llama a la función para resolver el Sudoku
#    return tablero  # Retorna el tablero resuelto

def generar_tablero_completo():
    """Genera un tablero de Sudoku completo válido."""
    tablero = [[0 for _ in range(9)] for _ in range(9)]  # Crea un tablero vacío

    def resolver(tablero):
        """Resuelve el tablero usando backtracking."""
        for fila in range(9):
            for col in range(9):
                if tablero[fila][col] == 0:  # Encuentra una celda vacía
                    numeros = list(range(1, 10))
                    random.shuffle(numeros)  # Mezcla los números para mayor aleatoriedad
                    for num in numeros:
                        if generar_subtablero(tablero, fila, col, num):  # Verifica si el número es válido
                            tablero[fila][col] = num  # Coloca el número en la celda
                            if resolver(tablero):  # Llama recursivamente a la función
                                return True
                            tablero[fila][col] = 0  # Backtrack si no se puede completar el tablero
                    return False  # Retorna False si no se puede colocar ningún número
        return True  # Retorna True si el tablero está completo

    resolver(tablero)  # Llama a la función resolver para generar el tablero
    return tablero

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
        "1": ("Súper fácil", 3/81),
        "2": ("Fácil", 0.30),
        "3": ("Medio", 0.45),
        "4": ("Difícil", 0.70)
    }

    print("\nSelecciona la dificultad:")
    for clave, (nombre, _) in niveles.items():
        print(f"{clave}. {nombre}")

    while True:
        opcion = input("Opción: ")
        if opcion in niveles:
            return niveles[opcion][1]
        print("Opción no válida, intenta nuevamente.")

def obtener_dificultad(mensaje, min_val, max_val):
    """Solicita un número al usuario y maneja errores."""
    while True:
        try:
            num = int(input(mensaje))
            if min_val <= num <= max_val:
                return num
            print(f"Error: Ingresa un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def jugar_sudoku():
    """Función principal para jugar Sudoku."""
    limpiar_pantalla()
    mostrar_titulo()

    tablero = generar_tablero_completo()  # Genera un tablero completo válido
    porcentaje_vacio = generar_dificultad()  # Solicita al usuario seleccionar la dificultad
    eliminar_numeros(tablero, porcentaje_vacio)  # Elimina números del tablero según la dificultad seleccionada

    while not all(0 not in fila for fila in tablero):  # Bucle que se ejecuta mientras el tablero no esté lleno
        limpiar_pantalla()
        mostrar_reglas()
        mostrar_titulo()
        imprimir_tablero(tablero)

        print("\nIngrese las coordenadas y el número a colocar:")

        fila = obtener_dificultad("Ingresa la fila (0-8): ", 0, 8)
        col = obtener_dificultad("Ingresa la columna (0-8): ", 0, 8)

        if tablero[fila][col] != 0:
            print("Error: La celda ya tiene un número. Intenta en otra posición.")
            continue

        num = obtener_dificultad("Ingresa un número (1-9): ", 1, 9)

        if generar_subtablero(tablero, fila, col, num):
            tablero[fila][col] = num
        else:
            print("Error: Número no válido en esta posición. Intenta de nuevo.")

    limpiar_pantalla()
    mostrar_titulo()
    imprimir_tablero(tablero)
    print("\n¡Felicidades! Has completado el Sudoku correctamente.")

def main():
    jugar_sudoku()

if __name__ == "__main__":
    main()