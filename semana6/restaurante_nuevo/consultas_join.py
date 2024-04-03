# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Consultar datos de Pedidos JOIN
print("\nPEDIDOS: INNER JOIN")

cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero, PEDIDOS.cantidad, PEDIDOS.fecha  
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)


# Consultar datos de pedidos LEFT JOIN
print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero
    FROM PLATOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
    LEFT JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id;
    """
)
for row in cursor:
    print(row)


