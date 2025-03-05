# Problema 3: Sudoku 🔢
```
Diseñe e implemente un juego de Sudoku en Python, donde el usuario debe completar un tablero de nivel fácil escogido aleatoriamente.
```

# Descripción
```
El programa selecciona un tablero de Sudoku entre cinco opciones disponibles. El usuario ingresa valores en coordenadas seleccionadas. Al final, se verifica si el tablero fue completado correctamente.
```

# Pseudocódigo 
```
Inicio
    Limpiar pantalla
    Mostrar título del juego

    Definir un tablero vacío de 9x9
    Llenar el tablero usando backtracking

    Mostrar opciones de dificultad
    Leer dificultad seleccionada
    Eliminar números del tablero según la dificultad

    Mientras el tablero no esté completo hacer
        Limpiar pantalla
        Mostrar reglas del Sudoku
        Mostrar título
        Imprimir el tablero

        Pedir al usuario la fila donde quiere ingresar un número
        Pedir al usuario la columna donde quiere ingresar un número

        Si la celda ya tiene un número entonces
            Mostrar mensaje de error
            Continuar con la siguiente iteración

        Pedir al usuario el número a colocar en la celda

        Si el número es válido según las reglas del Sudoku entonces
            Colocar el número en la celda
        Sino
            Mostrar mensaje de error

    Limpiar pantalla
    Mostrar título
    Imprimir tablero final
    Mostrar mensaje de éxito
Fin
```