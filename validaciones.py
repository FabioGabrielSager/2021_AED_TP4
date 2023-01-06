# Funcion para validar que un numero ingresado este comprendido dentro de un rango requerido por el programador
def cargar_y_validar_entre(lim_inf, lim_sup, msj_ingreso='Ingrese un valor: ', msj_error='ERROR ESE DATO NO EXISTE'):
    cantidad = int(input(msj_ingreso))

    # Mientras que la carga este fuera del limite requerido
    while cantidad < lim_inf or cantidad > lim_sup:
        print()
        print(msj_error)
        print()
        input('Presione enter para continuar')

        cantidad = int(input(msj_ingreso))

    return cantidad


# Funcion para validar que la carga de un numero sea mayor a un limite requerido por el programador
def cargar_y_validar_mayor_que(limite, msj_ingreso='Ingrese un valor: ', msj_error='ERROR LA CANTIDAD ES ERRONEA'):
    cantidad = int(input(msj_ingreso))

    # Mientras que la carga sea menor al limite requerido
    while cantidad < limite:
        print()
        print(msj_error)
        print()
        input('Presione enter para continuar')

        cantidad = int(input(msj_ingreso))

    return cantidad
