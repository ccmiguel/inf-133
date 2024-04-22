from flask import Blueprint, request, redirect, url_for
from views import user_view
from models.user_model import User
from datetime import datetime

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route('/users', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        birth_date_str = request.form['birth_date']  # Obtener la cadena de fecha
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()  # Convertir la cadena en objeto date
        # Creamos un nuevo usuario con los datos del formulario
        user = User(first_name=first_name, last_name=last_name, email=email, password=password, birth_date=birth_date)
        user.save()
        return redirect(url_for('user.usuarios'))
    return user_view.registro()
