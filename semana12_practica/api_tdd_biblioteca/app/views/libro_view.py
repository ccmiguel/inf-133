def render_libro_list(libros):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "id": libro.id,
            "autor": libro.autor,
            "titulo": libro.titulo,
            "edicion": libro.edicion,
            "disponibilidad": libro.disponibilidad,
        }
        for libro in libros
    ]

def render_libro_detail(libro):
    return {
        "id": libro.id,
        "autor": libro.autor,
        "titulo": libro.titulo,
        "edicion": libro.edicion,
        "disponibilidad": libro.disponibilidad,
    }
