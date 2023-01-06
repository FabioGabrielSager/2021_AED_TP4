import os.path

import interfaz
import registro_libro
import funciones


def procesar_archivo(nom_archivo):
    # Verificar si el archivo existe y si no existe cortar
    if not os.path.exists(nom_archivo):
        print('\n\nError: el arhivo no existe...\n\n\n')
        return None

    archivo = open("libros.csv", mode="rt", encoding="utf8")

    tam_archivo = os.path.getsize(nom_archivo)
    libros = []
    contador = 0

    # El siguiente par de variables solo corresponde a una custion de interfaz, son creadas para la utlizacion de la
    # funcion mostrar_carga_salteando_repetidos del modulo interfaz
    porcentaje_de_carga = 0
    porcentaje_de_carga_anterior = -1
    # Comienzo a leer línea por línea el archivo de texto
    while True:

        # Funcion para mostrar el porcentaje de carga actual del proceso
        interfaz.mostrar_carga_salteando_repetidos(porcentaje_de_carga, porcentaje_de_carga_anterior)

        contador += 1

        # Evito la linea de encabezado moviendo una linea el file pointer:
        if contador == 1:
            archivo.readline()

        linea = archivo.readline()

        if linea == '':
            break

        # eliminar el '\n' del final de linea.
        if linea[-1] == '\n':
            linea = linea[:-1]

        # a partir de la linea leida, obtener vector de cadenas con cada cadena separada
        cadenas = linea.split(sep=',')

        # crear el registro Libro
        libro = registro_libro.Libro(cadenas[0], int(cadenas[1]), int(cadenas[2]), int(cadenas[3]),
                                     float(cadenas[4]), cadenas[5])

        # agregar el registro al vector
        funciones.add_in_order(libros, libro)

        pos_fp = archivo.tell()
        porcentaje_de_carga_anterior = porcentaje_de_carga
        porcentaje_de_carga = int(funciones.calcular_porcentaje(pos_fp, tam_archivo))

    return libros
