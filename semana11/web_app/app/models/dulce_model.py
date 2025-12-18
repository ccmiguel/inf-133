from database import db
from datetime import datetime

class Dulce(db.Model):
    __tablename__ = "dulces"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    sabor = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_vencimiento = db.Column(db.Date, nullable=True)
    stock = db.Column(db.Integer, default=0)
    imagen_url = db.Column(db.String(255), nullable=True)
    disponible = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, marca, peso, sabor, origen, precio=None, 
                 descripcion=None, fecha_vencimiento=None, stock=0, 
                 imagen_url=None, disponible=True):
        self.nombre = nombre
        self.marca = marca
        self.peso = peso
        self.sabor = sabor
        self.origen = origen
        self.precio = precio
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.stock = stock
        self.imagen_url = imagen_url
        self.disponible = disponible

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Dulce.query.all()

    @staticmethod
    def get_by_id(id):
        return Dulce.query.get(id)

    @staticmethod
    def get_disponibles():
        return Dulce.query.filter_by(disponible=True).all()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None and hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()