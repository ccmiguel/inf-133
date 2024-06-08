def test_get_libros_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de libroes
    response = test_client.get("/api/libros", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro(test_client, admin_auth_headers):
    data = {"autor": "Gabriel Garcia Marquez", "titulo": "Cien anios de Soledad", "edicion": "Cuarta", "disponibilidad": "Prestado"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["autor"] == "Gabriel Garcia Marquez"
    assert response.json["titulo"] == "Cien anios de Soledad"
    assert response.json["edicion"] == "Cuarta"
    assert response.json["disponibilidad"] == "Prestado"


def test_get_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener un libro específico
    # Este test asume que existe al menos un libro en la base de datos
    response = test_client.get("/api/libros/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "autor" in response.json


def test_create_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un libro
    data = {"autor": "J. K. Rollings", "titulo": "Harry Potter la orden del fenix", "edicion": "Cuarta", "disponibilidad": "Disponible"}
    response = test_client.post("/api/libros", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_update_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un libro
    data = {"autor": "Gabriel Garcia Marquez", "titulo": "Cien anios de Soledad", "edicion": "Octava", "disponibilidad": "Prestado"}
    response = test_client.put("/api/libros/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_libro_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un libro
    response = test_client.delete("/api/libros/1", headers=user_auth_headers)
    assert response.status_code == 403