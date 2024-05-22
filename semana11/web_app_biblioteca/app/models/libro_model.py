from database import db

# Define la clase `Libro` que hereda de `db.Model`
# `Libro` representa la tabla `libros` en la base de datos
class Libro(db.Model):
    __tablename__ = "libros"

    # Define las columnas de la tabla `libros`
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    edicion = db.Column(db.String(100), nullable=False)
    disponibilidad = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `Libro`
    def __init__(self, id, autor, titulo, edicion, disponibilidad):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.edicion = edicion
        self.disponibilidad = disponibilidad

    # Guarda un libro en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los libros de la base de datos
    @staticmethod
    def get_all():
        return Libro.query.all()

    # Obtiene un libro por su ID
    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)

    # Actualiza un libro en la base de datos
    def update(self, autor=None, titulo=None, edicion=None, disponibilidad=None):
        if autor is not None:
            self.autor = autor
        if titulo is not None:
            self.titulo = titulo
        if edicion is not None:
            self.edicion = edicion
        if disponibilidad is not None:
            self.disponibilidad = disponibilidad
        db.session.commit()

    # Elimina un libro de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
