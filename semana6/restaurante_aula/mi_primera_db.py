# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Crear tabla de platos
conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    categoria TEXT NOT NULL);
    """
)

# Insertar datos de platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza',10.99,'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa',8.99,'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi',12.99,'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada',6.99,'Vegetariana')
    """
)

# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

# PLATOS:
# (1, 'Pizza', 10.99, 'Italiana')
# (2, 'Hamburguesa', 8.99, 'Americana')
# (3, 'Sushi', 12.99, 'Japonesa')
# (4, 'Ensalada', 6.99, 'Vegetariana')


# Crear tablas de mesas
conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTERGER NOT NULL);
    """
)

# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)

# Consultar datos de estudiantes
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

# ESTUDIANTES:
# (1, 1)
# (2, 2)
# (3, 3)
# (4, 4)

# Crear tabla de pedidos
conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)

# Insertar datos de pedidos
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 2, '2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (2, 3, 1, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (3, 1, 3, '2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (4, 4, 1, '2024-04-02')
    """
)

# Consultar datos de pedidos
print("\nPEDIDOS:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, PLATOS.precio, MESAS.numero, PEDIDOS.fecha 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)

# PEDIDOS:
# ('Pizza', 10.99, 2, '2024-04-01')
# ('Hamburguesa', 8.99, 3, '2024-04-01')
# ('Sushi', 12.99, 1, '2024-04-02')
# ('Ensalada', 6.99, 4, '2024-04-02')    





######################################################### EJERCICIO 1 ##################################################
# Actualizar una fila de la tabla de platos
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)
# Listar datos de pedidos
print("\nEJERCICIO_1:")
print("\nPLATOS:")
cursor = conn.execute(
    "SELECT * FROM PLATOS"
)
for row in cursor:
    print(row)
    
# PLATOS:
# (1, 'Pizza', 10.99, 'Italiana')
# (2, 'Hamburguesa', 9.99, 'Americana')
# (3, 'Sushi', 12.99, 'Fusion')
# (4, 'Ensalada', 6.99, 'Vegetariana')




######################################################## EJERCICIO 2 ######################################################
# Cambiar una fila de la tabla de platos
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)
# Listar datos de platos
print("\nEJERCICIO_2:")
print("\nPLATOS:")
cursor = conn.execute(
    "SELECT * FROM PLATOS"
)
for row in cursor:
    print(row)
    
# PLATOS:
# (1, 'Pizza', 10.99, 'Italiana')
# (2, 'Hamburguesa', 8.99, 'Americana')
# (3, 'Sushi', 12.99, 'Fusion')
# (4, 'Ensalada', 6.99, 'Vegetariana')



################################################### EJERCICIO 3 ########################################################
# Eliminar una fila de la tabla de platos
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id = 4
    """
)

# Listar datos de pedidos
print("\nEJERCICIO_3:")
print("\nPLATOS:")
cursor = conn.execute(
    "SELECT * FROM PLATOS"
)

for row in cursor:
    print(row)

# PLATOS:
# (1, 'Pizza', 10.99, 'Italiana')
# (2, 'Hamburguesa', 8.99, 'Americana')
# (3, 'Sushi', 12.99, 'Fusion') 




######################################################### EJERCICIO 4 ######################################################
# Eliminar una fila de la tabla de pedidos
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)

# Listar datos de pedidos
print("\nEJERCICIO_4:")
print("\nPEDIDOS:")
cursor = conn.execute(
    "SELECT * FROM PEDIDOS"
)

for row in cursor:
    print(row)

# PEDIDOS:
# (1,'Pizza', 10.99, 2, '2024-04-01')
# (2,'Hamburguesa', 8.99, 3, '2024-04-01')
# (4,'Ensalada', 6.99, 4, '2024-04-02')   



# Cerrar conexión
conn.close()