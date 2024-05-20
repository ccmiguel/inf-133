from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.libro_model import Libro
from views import libro_view

# Importamos el decorador de roles
from utils.decorators import role_required

libro_bp = Blueprint("libro", __name__)


@libro_bp.route("/libros")
@login_required
def list_libros():
    libros = Libro.get_all()
    return libro_view.list_libros(libros)


@libro_bp.route("/libros/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_libro():
    if request.method == "POST":
        if current_user.has_role("admin"):
            id = int(request.form["id"])
            autor = request.form["autor"]
            titulo = request.form["titulo"]
            edicion = request.form["edicion"]
            disponibilidad = request.form["disponibilidad"]
            libro = Libro(id=id,autor=autor,titulo=titulo,edicion=edicion, disponibilidad=disponibilidad)
            libro.save()
            flash("Libro creado exitosamente", "success")
            return redirect(url_for("libro.list_libros"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return libro_view.create_libro()


@libro_bp.route("/libros/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_libro(id):
    libro = libro.get_by_id(id)
    if not libro:
        return "Libro no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            id = int(request.form["id"])
            autor = request.form["autor"]
            titulo = request.form["titulo"]
            edicion = request.form["edicion"]
            disponibilidad = request.form["disponibilidad"]
            libro.update(id=id,autor=autor,titulo=titulo,edicion=edicion, disponibilidad=disponibilidad)
            flash("Libro actualizado exitosamente", "success")
            return redirect(url_for("libro.list_libros"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return libro_view.update_libro(libro)


@libro_bp.route("/libros/<int:id>/delete")
@login_required
@role_required("admin")
def delete_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        return "Libro no encontrado", 404
    if current_user.has_role("admin"):
        libro.delete()
        flash("Libro eliminado exitosamente", "success")
        return redirect(url_for("libro.list_libros"))
    else:
        return jsonify({"message": "Unauthorized"}), 403