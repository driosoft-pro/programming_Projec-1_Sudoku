# Proyecto: Juegos en Python 🎮

Este repositorio contiene el desarrollo del **Proyecto 1** de la asignatura **Programación (G02)**, correspondiente a la **Facultad de Ingeniería y Ciencias Básicas** en el **Programa Académico de Ingeniería de Datos e Inteligencia Artificial**.

## 📌 Objetivos
- Familiarizarse con las fases de desarrollo de software: **análisis, pseudocódigo, codificación, pruebas, depuración y documentación**.
- Aplicar el uso de **funciones, estructuras de decisión y repetitivas** en Python.

## 📋 Metodología
- El proyecto debe ser desarrollado en **grupos de 3 a 4 personas**.
- Para cada problema, los entregables son:
  1. **Análisis del problema**.
  2. **Algoritmo en pseudocódigo**.
  3. **Implementación funcional en Python**.
  4. **Evidencias de ejecución del programa** (capturas de pantalla).

## 📂 Entregables
- **📄 Informe en PDF (30%)**: Contiene análisis, pseudocódigo y capturas de pantalla.
- **💻 Código en Python (40%)**: Implementado en Jupyter Notebook y subido a GitHub.
- **🎤 Sustentación (30%)**: Se realizará el **jueves 06 de marzo de 2025** en horario de clase.

## 🕹️ Problema a Resolver

### **Problema 3: Sudoku** 🔢
- Se almacenan **5 tableros de Sudoku** de nivel **fácil**.
- Se selecciona un tablero aleatoriamente.
- El usuario **ingresa números** y coordenadas para resolverlo.
- Se verifica si las jugadas son **correctas o incorrectas**.
- Al final, se indica si el usuario **ganó**.

## 📂 Estructura del Repositorio
``` 
│── README.md # Documentación del proyecto
│── informe.pdf # Documento con análisis, pseudocódigo y capturas
└── problema_3/
  |─- sudoku.py # Código de Sudoku
  └── pseudocodigo.md # Pseudocódigo del problema 3
 
```
======================================================================
```
===========================================================================
                             REGLAS DEL SUDOKU
===========================================================================
1. Se genera un tablero de Sudoku 9x9 con algunos espacios vacíos.
2. Debes rellenar los espacios vacíos con números del 1 al 9.
3. No puedes repetir números en la misma fila, columna o subcuadrícula 3x3.
4. Ganas cuando completas el tablero correctamente.
5. Guia de ingreso de datos C para columnas y F para Filas
===========================================================================
===========================================================================
                               JUEGO DE SUDOKU
===========================================================================

  C 0 1 2 | 3 4 5 | 6 7 8
F ┌-----------------------┐
0 | 1 2 3 | . . . | 7 8 . |
1 | 4 5 6 | . . 9 | 1 . 3 |
2 | 7 8 9 | . 2 . | 4 5 6 |
  |-------|-------|-------|
3 | 2 1 4 | 3 6 5 | . 9 7 |
4 | 3 . 5 | 8 9 7 | . 1 4 |
5 | 8 . . | 2 . 4 | 3 6 5 |
  |-------|-------|-------|
6 | . 3 1 | 6 4 2 | 9 . 8 |
7 | 6 4 2 | . 7 8 | 5 . . |
8 | 9 7 . | . . 1 | . 4 2 |
  └-----------------------┘

Ingrese las coordenadas y el número a colocar:
Ingresa la fila (0-8):
```
======================================================================

## 🚀 Cómo Ejecutar los Juegos
1. Clona este repositorio:
   ```bash
   git clone https://github.com/driosoft-pro/programming_Projec-1_Sudoku.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd nombre-del-repositorio
   ```
3. Ejecuta cada juego con Python:
   ```bash
   python sudoku.py
   ```


## 🛠 Requisitos
- Python 3.x
- No se requiere instalación de librerías adicionales

## 📜 Licencia
Este proyecto está bajo la licencia MIT - Puedes usarlo libremente. 😊

---
¡Esperamos que disfrutes estos juegos en Python! 🚀

## Autor
📌 **By:** Deyton Riascos Ortiz
            Dana Isabella Mosquera Mosquera
            Samuel Izquierdo Bonilla 