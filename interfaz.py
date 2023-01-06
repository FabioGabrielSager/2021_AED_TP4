import funciones
import validaciones


def menu_principal():
    menu = '\n              ■■■■■MENU PRINCIPAL■■■■■' \
           '\n1.Cargar el contenido del archivo en un vector de registros de libros' \
           '\n2.Buscar un libro para revision mediante ISBN o titulo' \
           '\n3.Buscar en el vector el libro con mayor cantidad de revisiones. Informar si su rating es mayor,\n' \
           '  menor o igual al rating promedio de su mismo idioma.' \
           '\n4.A partir del vector, generar una matriz donde cada fila sea un idioma y cada columna un año de\n' \
           '  publicación. Cada celda contendra el mayor rating (solo para el rango de años 2000-2020 incluidos)' \
           '\n5.A partir del vector, generar un vector de conteo donde cada celda representa una década entre 1900 y\n' \
           '  2000. Cada celda indicara cuántos libros se publicaron en esa década.' \
           '\n6.Almacenar contenido de la matriz registros por registro (omitiendo las celdas vacías) en un archivo\n' \
           '  binario llamado populares.dat e informar la cantidad de registros grabados' \
           '\n7.Mostrar archivo generado en el punto anterior' \
           '\n0.Salir del programa' \
           '\nIngrese la opcion deseada: '

    opcion = validaciones.cargar_y_validar_entre(0, 7, menu, 'ERROR, ESA OPCION NO EXISTE')

    return opcion


def menu_para_op_2():
    eleccion = '\n              ■■■■■BUSQUEDA DE LIBROS■■■■■' \
               '\n1.Buscar por isbn' \
               '\n2.Buscar por titulo' \
               '\n3.Salir al menu principal' \
               '\nIngrese la opcion deseada: '
    opcion = validaciones.cargar_y_validar_entre(1, 3, eleccion, 'ERROR, ESA OPCION NO EXISTE')

    return opcion


def presione_enter_para(para='continuar'):
    input(f'Presione enter para {para}')


# Funcion creada para ser utilizada en la muetra de un proceso de carga porcentaje, se encarga de mostrar solo aquellos
# orcentajes distintos del anterior
def mostrar_carga_salteando_repetidos(porcentaje_de_carga, porcentaje_de_carga_anterior, en_linea=True):
    if porcentaje_de_carga != porcentaje_de_carga_anterior:
        if en_linea:
            if porcentaje_de_carga != 100:
                print(f'{porcentaje_de_carga}%', end=' ')
            else:
                print(f'{porcentaje_de_carga}%')
        else:
            print(f'{porcentaje_de_carga}%')


def mostrar_resultados_op_3(libro_may_revs, prom_de_rating_x):
    print()
    print(f'El libro con mas cantidad de revisiones es: {libro_may_revs.titulo} con: '
          f'{libro_may_revs.cant_revisiones} revisiones')

    print()
    if libro_may_revs.rating < prom_de_rating_x:
        print(f'El libro, {libro_may_revs.titulo}, tiene un rating menor al promedio de '
              f'ratings de los libros con idioma: '
              f'{libro_may_revs.idioma}')

    elif libro_may_revs.rating > prom_de_rating_x:
        print(f'El libro, {libro_may_revs.titulo}, tiene un rating mayor al promedio de '
              f'ratings de los libros con idioma: '
              f'{libro_may_revs.idioma}')

    else:
        print(f'El libro, {libro_may_revs.titulo}, tiene un rating igual al promedio de '
              f'ratings de los libros con idioma: '
              f'{libro_may_revs.idioma}')
    print(f'Rating libro: {libro_may_revs.rating}, '
          f'Raiting promedio por idioma: {prom_de_rating_x}')


def mostrar_vec_conteo_decadas(vec_conteo_decadas):
    for i in range(len(vec_conteo_decadas)):
        if vec_conteo_decadas[i] != 0:
            print(f'Decada {i + 1} ({((i + 190) * 10) + 1}-{((i + 1) + 190) * 10}): {vec_conteo_decadas[i]}')


def mostrar_decada_con_mas_publicaciones(vec_conteo_decadas):
    pos = funciones.buscar_mayor_in_vec(vec_conteo_decadas)

    print('Las decadas (entre 1900 y 2000) con mas revisiones son: ')
    for j in pos:
        print(f'{((j + 190) * 10) + 1}-{((j + 1) + 190) * 10} con {vec_conteo_decadas[j]} revisiones')
