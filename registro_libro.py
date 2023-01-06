class Libro:
    def __init__(self, titulo, cant_revisiones, ano_publicacion, idioma, rating, isbn):
        self.titulo = titulo
        self.cant_revisiones = cant_revisiones
        self.ano_publicacion = ano_publicacion
        self.idioma = idioma
        self.rating = rating
        self.isbn = isbn


def to_string(libro):
    rating = round(libro.rating, 2)
    renglon = ''
    renglon += '{:<200}'.format('Titulo: ' + libro.titulo)
    renglon += '{:<32}'.format('Cantidad de revisiones: ' + str(libro.cant_revisiones))
    renglon += '{:<26}'.format('Año de publicacion: ' + str(libro.ano_publicacion))
    renglon += '{:<14}'.format('Idioma: ' + str(libro.idioma))
    renglon += '{:<19}'.format('Rating: ' + str(rating))
    renglon += '{:<13}'.format('ISBN: ' + libro.isbn)

    return renglon
