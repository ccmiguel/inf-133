# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

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
    WHERE id = 3
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
