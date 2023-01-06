import funciones
import interfaz
from interfaz import presione_enter_para
import procesar_archivo
import registro_libro


def principal():
    # Nombre del archivo de texto a analizar
    nombre_archivo = 'libros.csv'
    op = -1
    vec_libros = None
    mat = None

    # Mientras que la opcion ingresada sea distinta a la opcion de salida del programa
    while op != 0:
        op = interfaz.menu_principal()

        # Se valida que el vector de libros contenga libros antes de ejecutar una opcion que requierea de esto
        if op != 1 and op != 0 and vec_libros is None:
            print()
            print('ERROR, PRIMERO DEBE CARGAR EL VECTOR DE LIBROS HACIENDO USO DE LA OPCION 1')
            presione_enter_para()

        elif op == 1:
            print('Cargando libros...')
            vec_libros = procesar_archivo.procesar_archivo(nombre_archivo)
            print('Libros cargados...')
            presione_enter_para()

        elif op == 2:
            # Sub-menu
            eleccion = -1

            # Mientras que la opcion sea distinta de la opcion de volver a menu principal
            while eleccion != 3:
                eleccion = interfaz.menu_para_op_2()
                print()
                if eleccion == 1:
                    isbn_a_buscar = input('Ingrese el ISBN del libro a buscar: ')
                    pos_isbn_a_buscar = funciones.buscar_libro_por_isbn(vec_libros, isbn_a_buscar)
                    print()
                    if pos_isbn_a_buscar != -1:
                        print('Libro encontrando, mostrando datos...')
                        print(registro_libro.to_string(vec_libros[pos_isbn_a_buscar]))
                        vec_libros[pos_isbn_a_buscar].cant_revisiones += 1
                        presione_enter_para()

                    else:
                        print(F'ERROR, EL LIBRO DE ISBN {isbn_a_buscar} NO SE ENCUENTRA REGISTRADO')
                        presione_enter_para()

                elif eleccion == 2:
                    titulo_a_buscar = input('Ingrese el titulo a buscar: ')
                    pos_titulo_a_buscar = funciones.buscar_libro_por_titulo(vec_libros, titulo_a_buscar)
                    print()
                    if pos_titulo_a_buscar != -1:
                        print('Libro encontrando, mostrando datos...')
                        print(registro_libro.to_string(vec_libros[pos_titulo_a_buscar]))
                        vec_libros[pos_titulo_a_buscar].cant_revisiones += 1
                        presione_enter_para()

                    else:
                        print(F'ERROR, EL LIBRO DE TITULO {titulo_a_buscar} NO SE ENCUENTRA REGISTRADO')
                        presione_enter_para()

        elif op == 3:
            pos_libro_may_cant_rev = funciones.buscar_libro_con_mas_revisiones(vec_libros)
            prom_de_rating_x = funciones.calcular_rating_promedio_de_idioma_x(vec_libros[pos_libro_may_cant_rev].idioma,
                                                                              vec_libros)

            interfaz.mostrar_resultados_op_3(vec_libros[pos_libro_may_cant_rev], prom_de_rating_x)

            print()
            presione_enter_para()

        elif op == 4:
            print()
            print('Generando matriz...')
            mat = funciones.matriz_punto_4(vec_libros)
            print()
            print('Matriz generada...')
            presione_enter_para()
            print()

        elif op == 5:
            print()
            vec_cont = funciones.contar_publis_x_decada_siglo_xx(vec_libros)
            interfaz.mostrar_vec_conteo_decadas(vec_cont)
            interfaz.mostrar_decada_con_mas_publicaciones(vec_cont)
            presione_enter_para()

        elif op == 6:
            print()
            # Si la matriz a procesar no fue creada
            if mat is None:
                print('ERROR, PRIMERO DEBE GENERAR LA MATRIZ MEDIANTE LA OPCION 4')
                presione_enter_para()

            # Si la matriz a procesar fue creada
            else:
                print('Cargando libros en archivo populares.dat...')
                funciones.generar_archivo('populares.dat', mat)
                print()
                print('Archivos cargados...')
                presione_enter_para()

        elif op == 7:
            print()
            print('Mostrando archivo...')
            funciones.mostrar_archivo_punto_6('populares.dat')
            presione_enter_para()

        elif op == 0:
            print()
            print('Gracias por utilizar este programa, adios! (-̀ᴗ-́)و')
            presione_enter_para('finalizar')


if __name__ == '__main__':
    principal()
