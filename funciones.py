import os.path
import pickle
import interfaz
import registro_libro


def calcular_porcentaje(cant_menor, cant_mayor):
    porcentaje = (cant_menor * 100) / cant_mayor
    return porcentaje


def add_in_order(vec_libros, libro):
    izq, der = 0, len(vec_libros) - 1
    pos = len(vec_libros)
    while izq <= der:
        c = (izq + der) // 2

        if libro.isbn == vec_libros[c].isbn:
            pos = c
            break

        elif libro.isbn < vec_libros[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec_libros[pos:pos] = [libro]


# Algoritmo de busqueda por ibsn, se utiliza busqueda binaria aprovecancho el orden por
# defecto que tendra el vector de libros a analizar
def buscar_libro_por_isbn(vec, isbn_a_buscar):
    izq, der = 0, len(vec) - 1

    while izq <= der:
        c = (izq + der) // 2

        if isbn_a_buscar == vec[c].isbn:
            return c

        elif isbn_a_buscar < vec[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    return -1


# Algoritmo de busqueda de libro por titulo, ya que el vector libros no posee ordenamiento por titulo,
# se aplico una busqueda secuencial
def buscar_libro_por_titulo(vec_libros, titulo_a_buscar):
    for i in range(len(vec_libros)):
        if vec_libros[i].titulo == titulo_a_buscar:
            return i

    return -1


# Funcion para la busqueda del registro libro con mayor cantidad de revisiones dentro de un
# vector de registros libros
def buscar_libro_con_mas_revisiones(vec_libros):
    cant_rev_may = pos_cant_rev_may = 0

    for i in range(len(vec_libros)):
        if vec_libros[i].cant_revisiones > cant_rev_may:
            cant_rev_may = vec_libros[i].cant_revisiones
            pos_cant_rev_may = i

    # Se retorna la posicion que ocupa el libro dentro del vector
    return pos_cant_rev_may


# Funcion para el calculo del rating promedio de un conjunto de libros con un idioma en comun (parametro idioma)
def calcular_rating_promedio_de_idioma_x(idioma, vec_libros):
    cont_rating = acu_rating = 0

    for libro in vec_libros:
        if libro.idioma == idioma:
            cont_rating += 1
            acu_rating += libro.rating

    rating_promedio = round(acu_rating / cont_rating, 2)

    return rating_promedio

# Funcion para la generacion de una matriz.
# Parametros formales
# n = filas
# m = columnas
# elemento_incial = elemento con el cual se rellena por defecto cada celda de la matriz
def generar_matriz(n, m, elemento_incial):
    mat = [[elemento_incial] * m for f in range(n)]
    return mat


# Funcion para generacion de matriz para la resolucion del punto numero 4 del enunciado
# Parametros formales:
# vec_libros = vector de registros libros
# imprimir_carga = Bandera o interruptor para indicar si se quieres una salida por pantalla del proceso de carga
# de la matriz
def matriz_punto_4(vec_libros, imprimir_carga=True):
    # Se genera una matriz de idiomas x años de publicacion ponderados
    mat = generar_matriz(27, 21, None)

    n = len(vec_libros)

    # El siguiente par de variables solo corresponde a una custion de interfaz, son creadas para la utlizacion de la
    # funcion mostrar_carga_salteando_repetidos del modulo interfaz
    porcentaje_de_carga = 0
    porcentaje_de_carga_anterior = -1

    for i in range(n):
        # Si se quiere imprimir en pantalla el porcentaje de carga de la matriz
        if imprimir_carga:
            interfaz.mostrar_carga_salteando_repetidos(porcentaje_de_carga, porcentaje_de_carga_anterior)
            porcentaje_de_carga_anterior = porcentaje_de_carga
            porcentaje_de_carga = int(calcular_porcentaje(i, n))

        # Si el año de publicacion del libro esta dentro del rango ponderado
        if 1999 < vec_libros[i].ano_publicacion < 2021:
            # Se determina fila y columna de la matriz a cargar
            fila = vec_libros[i].idioma - 1
            columna = vec_libros[i].ano_publicacion - 2000

            # Si en esa celda todavia no se cargo nada
            if mat[fila][columna] is None:
                mat[fila][columna] = vec_libros[i]

            # Si el rating del libro analizado actualmente es mayor al rating del libro contenido en la celda
            # de la matriz
            elif mat[fila][columna].rating < vec_libros[i].rating:
                # El libro mayor se guarda en la celda pisando al libro menor a el que antes yacia ahí
                mat[fila][columna] = vec_libros[i]

    return mat


# Funcion para contar la cantidad de publicaciones realizadas por decada durante el siglo 20
def contar_publis_x_decada_siglo_xx(vec_libros):
    vec_cont = [0] * 10

    for i in range(len(vec_libros)):
        # Se establece el rango del siglo xx para la cuenta de decadas (desde el primer año terminado en 1
        # hasta el primer año terminado en 0)
        if 1900 < vec_libros[i].ano_publicacion < 2001:
            # Ecuacion para la determinacion del indice segun el año de publicacion analizado para el acceso derecto
            # al vector de conteo. Ejemplo, si el libro esta entre el año 1901 y 1910 este corresponte a la
            # primer decada del siglo
            indice = ((vec_libros[i].ano_publicacion - 1) // 10) - 190
            vec_cont[indice] += 1

    return vec_cont


# Funcion para encontrar el o los valores mayores con mayor contenidos dentro de un vector
def buscar_mayor_in_vec(vector):
    may_cant_decada = 0
    # Se hace uso de un vector para guardar indices en caso de que hubise dos valores o mas con
    # las mismas cantidad
    pos = []

    for i in range(len(vector)):
        if may_cant_decada < vector[i]:
            may_cant_decada = vector[i]
            pos = [i]
        elif may_cant_decada == vector[i]:
            pos.append(i)

    return pos


# Funcion para la carga de registros libros a un archivo. Especificamente se hace la carga desde la matriz de
# registros generada como parte del punto 4 del enunciado
def generar_archivo(nombre_archivo, mat):
    # Se crea o abre (borrando contenido anterior) un archivo binario para la carga de libros
    m = open(nombre_archivo, 'wb')

    # Recorrido de matriz por filas
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            # Si la matriz contiene un registro libro
            if not mat[i][j] is None:
                # Se graba en el registro anter creado o abierto ayudandose del modulo pickle para la serialización
                pickle.dump(mat[i][j], m)

    m.close()


# Funcion para el recorrido y muestra del contenido del archivo generado en el punto numero 6 del enuciado,
# (archivo que contiene los libros mas populares)
def mostrar_archivo_punto_6(nombre_archivo):
    # Se verifica que el archivo a procesar exista segun la ruta indicada
    if not os.path.exists(nombre_archivo):
        print(f'El archivo {nombre_archivo} no fue creado.')
        return

    # Si el archivo existe se abre en modo lectura binaria
    m = open(nombre_archivo, 'rb')
    tam = os.path.getsize(nombre_archivo)

    # Se recorre el archivo (mientras que el valor del file pointer se menor al tamaño total del archivo)
    while m.tell() < tam:
        # Se recupera a memoria el libro leido del archivo mediante el modulo pickle
        libro_popular = pickle.load(m)
        # Se muestran datos del registro recuperado del archivo
        print(registro_libro.to_string(libro_popular))

    m.close()
