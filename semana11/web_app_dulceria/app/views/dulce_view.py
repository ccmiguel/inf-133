from flask import render_template
from flask_login import current_user


def list_dulces(dulces):
    return render_template(
        "dulces.html",
        dulces=dulces,
        title="Lista de dulces",
        current_user=current_user,
    )


def create_dulce():
    return render_template(
        "create_dulce.html", title="Crear Dulce", current_user=current_user
    )


def update_dulce(dulce):
    return render_template(
        "update_dulce.html",
        title="Editar Dulce",
        dulce=dulce,
        current_user=current_user,
    )
