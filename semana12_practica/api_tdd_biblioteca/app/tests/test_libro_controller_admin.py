def test_get_libros(test_client, admin_auth_headers):
    response = test_client.get("/api/libros", headers=admin_auth_headers)
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


def test_get_libro(test_client, admin_auth_headers):
    # Primero crea un libro
    data = {"autor": "Miguel de Cervantes", "titulo": "El Quijote", "edicion": "Segunda", "disponibilidad": "Disponible"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora obtén el libro
    response = test_client.get(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["autor"] == "Miguel de Cervantes"
    assert response.json["titulo"] == "El Quijote"
    assert response.json["edicion"] == "Segunda"
    assert response.json["disponibilidad"] == "Disponible"


def test_get_nonexistent_libro(test_client, admin_auth_headers):
    response = test_client.get("/api/libros/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_create_libro_invalid_data(test_client, admin_auth_headers):
    data = {"autor": "Antoine Exupery"}  # Falta titulo y edicion
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_libro(test_client, admin_auth_headers):
    # Primero crea un libro
    data = {"autor": "Antoine Exupery", "titulo": "El principito", "edicion": "Primera", "disponibilidad": "Disponible"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora actualiza el libro
    update_data = {"autor": "Antoine de Saint-Exupery", "titulo": "El principito", "edicion": "Primera", "disponibilidad": "Disponible"}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=admin_auth_headers
    )
    assert response.status_code == 200
    assert response.json["autor"] == "Antoine de Saint-Exupery"
    assert response.json["titulo"] == "El principito"
    assert response.json["edicion"] == "Primera"
    assert response.json["disponibilidad"] == "Disponible"


def test_update_nonexistent_libro(test_client, admin_auth_headers):
    update_data = {"autor": "Carlos Cuautemoc", "titulo": "Juventud en Extasis", "edicion": "Quinta", "disponibilidad": "Disponible" }
    response = test_client.put(
        "/api/libros/999", json=update_data, headers=admin_auth_headers
    )
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_delete_libro(test_client, admin_auth_headers):
    # Primero crea un libro
    data = {"autor": "Benito Perez Galdos", "titulo": "Marianela", "edicion": "Cuarta", "disponibilidad": "Prestado"}
    response = test_client.post("/api/libros", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    # Ahora elimina el libro
    response = test_client.delete(
        f"/api/libros/{libro_id}", headers=admin_auth_headers
    )
    assert response.status_code == 204

    # Verifica que el libro ha sido eliminado
    response = test_client.get(f"/api/libros/{libro_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"


def test_delete_nonexistent_libro(test_client, admin_auth_headers):
    response = test_client.delete("/api/libros/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Libro no encontrado"