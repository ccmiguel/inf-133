from flask import Blueprint, request, redirect, url_for, flash, jsonify, current_app
from flask_login import login_required, current_user
from models.dulce_model import Dulce
from views import dulce_view
from utils.decorators import role_required
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import uuid
import sys

dulce_bp = Blueprint("dulce", __name__)

# --- CONFIGURACIÓN CORREGIDA ---
# Obtiene la ruta absoluta del directorio donde está este archivo (controllers/)
CONTROLLER_DIR = os.path.dirname(os.path.abspath(__file__))
# Sube un nivel para llegar a 'app/', y luego otro para llegar a la raíz del proyecto ('web_app_dulceria2/')
PROJECT_ROOT = os.path.dirname(os.path.dirname(CONTROLLER_DIR))

# Configuración de imágenes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
# Define la ruta ABSOLUTA a la carpeta de uploads
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'static', 'uploads', 'dulces')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(file):
    """Guarda la imagen y retorna la ruta"""
    if file and allowed_file(file.filename):
        
        # Obtener la carpeta de uploads desde la configuración
        upload_folder = os.path.join('..', current_app.config['UPLOAD_FOLDER'])

        # Crear carpeta si no existe
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        
        # Generar nombre único
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        
        # Guardar archivo
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(file_path)
        
        return f"uploads/dulces/{unique_filename}"
    return None

def delete_image(image_path):
    """Elimina la imagen del sistema de archivos"""
    if image_path:
        full_path = os.path.join('static', image_path)
        if os.path.exists(full_path):
            os.remove(full_path)

@dulce_bp.route("/dulces")
@login_required
def list_dulces():  # CAMBIA: de list_dulces_route a list_dulces
    dulces = Dulce.get_all()
    
    # DEBUG: Ver información de imágenes
    for dulce in dulces:
        print(f"Dulce: {dulce.nombre}")
        print(f"  URL en BD: {dulce.imagen_url}")
        if dulce.imagen_url:
            # Construir ruta completa
            static_path = os.path.join('..', 'static', dulce.imagen_url)
            print(f"  Ruta física: {os.path.abspath(static_path)}")
            print(f"  ¿Existe?: {os.path.exists(os.path.abspath(static_path))}")
            
    return dulce_view.list_dulces(dulces)


@dulce_bp.route("/dulces/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_dulce():
    if request.method == "POST":
        try:
            # Obtener datos del formulario
            nombre = request.form.get("nombre")
            marca = request.form.get("marca")
            peso = float(request.form.get("peso", 0))
            sabor = request.form.get("sabor")
            origen = request.form.get("origen")
            precio = float(request.form.get("precio", 0)) if request.form.get("precio") else None
            descripcion = request.form.get("descripcion")
            stock = int(request.form.get("stock", 0))
            
            # Procesar fecha de vencimiento
            fecha_vencimiento_str = request.form.get("fecha_vencimiento")
            fecha_vencimiento = None
            if fecha_vencimiento_str:
                try:
                    fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, '%Y-%m-%d').date()
                except ValueError:
                    pass
            
            # Procesar imagen
            imagen_url = None
            if 'imagen' in request.files:
                file = request.files['imagen']
                if file.filename != '':  # Verificar que se subió un archivo
                    imagen_url = save_image(file)
            
            # Después de procesar la imagen, agrega:
            print(f"Imagen subida: {file.filename}")
            print(f"Extensión: {file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else 'No tiene extensión'}")
            print(f"¿Está permitida?: {allowed_file(file.filename)}")
            print(f"Ruta guardada: {imagen_url}")
            
            # Crear dulce
            dulce = Dulce(
                nombre=nombre,
                marca=marca,
                peso=peso,
                sabor=sabor,
                origen=origen,
                precio=precio,
                descripcion=descripcion,
                fecha_vencimiento=fecha_vencimiento,
                stock=stock,
                imagen_url=imagen_url
            )
            
            dulce.save()
            flash("Dulce creado exitosamente", "success")
            return redirect(url_for("dulce.list_dulces"))
            
        except Exception as e:
            flash(f"Error al crear dulce: {str(e)}", "error")
            return redirect(url_for("dulce.create_dulce"))
    
    return dulce_view.create_dulce()

@dulce_bp.route("/dulces/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        flash("Dulce no encontrado", "error")
        return redirect(url_for("dulce.list_dulces"))
    
    if request.method == "POST":
        try:
            # Obtener datos del formulario
            update_data = {
                "nombre": request.form.get("nombre"),
                "marca": request.form.get("marca"),
                "peso": float(request.form.get("peso", 0)),
                "sabor": request.form.get("sabor"),
                "origen": request.form.get("origen"),
                "precio": float(request.form.get("precio", 0)) if request.form.get("precio") else None,
                "descripcion": request.form.get("descripcion"),
                "stock": int(request.form.get("stock", 0)),
                "disponible": request.form.get("disponible") == "on"
            }
            
            # Procesar fecha de vencimiento
            fecha_vencimiento_str = request.form.get("fecha_vencimiento")
            if fecha_vencimiento_str:
                try:
                    update_data["fecha_vencimiento"] = datetime.strptime(fecha_vencimiento_str, '%Y-%m-%d').date()
                except ValueError:
                    pass
            else:
                update_data["fecha_vencimiento"] = None
            
            # Procesar imagen nueva
            if 'imagen' in request.files:
                file = request.files['imagen']
                if file and file.filename != '':
                    # Eliminar imagen anterior si existe
                    if dulce.imagen_url:
                        delete_image(dulce.imagen_url)
                    
                    # Guardar nueva imagen
                    imagen_url = save_image(file)
                    update_data["imagen_url"] = imagen_url
            
            dulce.update(**update_data)
            flash("Dulce actualizado exitosamente", "success")
            return redirect(url_for("dulce.list_dulces"))
            
        except Exception as e:
            flash(f"Error al actualizar dulce: {str(e)}", "error")
    
    return dulce_view.update_dulce(dulce)

@dulce_bp.route("/dulces/<int:id>/delete")
@login_required
@role_required("admin")
def delete_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        flash("Dulce no encontrado", "error")
        return redirect(url_for("dulce.list_dulces"))
    
    # Eliminar imagen asociada
    if dulce.imagen_url:
        delete_image(dulce.imagen_url)
    
    dulce.delete()
    flash("Dulce eliminado exitosamente", "success")
    return redirect(url_for("dulce.list_dulces"))