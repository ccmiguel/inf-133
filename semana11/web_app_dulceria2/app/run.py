from flask import Flask, redirect, url_for
from flask_login import LoginManager
import os

# Importamos los controladores y modelos
from controllers import user_controller, dulce_controller
from database import db
from models.user_model import User

# Inicializa la aplicación Flask
app = Flask(__name__, 
            template_folder='templates',
            static_folder='../static')

# Configuración de la base de datos - VUELVE A TU CONFIGURACIÓN ORIGINAL
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dulce.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"

# Configuración para subida de archivos
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads', 'dulces')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB límite

# Crear carpetas necesarias
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('../static/images', exist_ok=True)

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.init_app(app)

# Función para cargar un usuario basado en su ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Inicializa `db` con la aplicación Flask
db.init_app(app)

# Registra los Blueprints
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(dulce_controller.dulce_bp)

# Ruta principal
@app.route('/')
def index():
    return redirect(url_for("dulce.list_dulces"))  # Cambia a list_dulces

if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    
    # Verificar si existe imagen por defecto
    default_image = '../static/images/default_candy.jpg'
    if not os.path.exists(default_image):
        try:
            # Crear una imagen por defecto simple
            from PIL import Image, ImageDraw
            img = Image.new('RGB', (300, 200), color='pink')
            d = ImageDraw.Draw(img)
            d.text((100, 100), "Sin Imagen", fill='white')
            img.save(default_image)
            print(f"Imagen por defecto creada: {default_image}")
        except ImportError:
            print("Pillow no está instalado. Instala con: pip install Pillow")
    
    print("Aplicación iniciando en http://localhost:5000")
    app.run(debug=True)