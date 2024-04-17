# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

######################################################### EJERCICIO 1 ##################################################
# Actualizar una fila de la tabla de empleados
conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 1
    WHERE id = 2
    """
)
# Listar datos de tabla
print("\nEJERCICIO_1:")
print("\nEMPLEADOS:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombre, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    """
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
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 1
    """
)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombre, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario  
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    JOIN SALARIOS ON SALARIOS.empleado_id = EMPLEADOS.id 
    """
)
for row in cursor:
    print(row)




################################################### EJERCICIO 3 ########################################################
# Eliminar una fila de la tabla de empleados
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

# Listar datos de pedidos
print("\nEJERCICIO_3:")
print("\nEMPLEADOS:")
cursor = conn.execute(
    "SELECT * FROM EMPLEADOS"
)

for row in cursor:
    print(row)

# PLATOS:
# (1, 'Pizza', 10.99, 'Italiana')
# (2, 'Hamburguesa', 8.99, 'Americana')
# (3, 'Sushi', 12.99, 'Fusion') 



######################################################### EJERCICIO 4 ######################################################
conn.execute(
    """
    INSERT INTO EMPLEADOS (departamento_id, cargo_id, nombre, apellido_paterno, apellido_materno, fecha_contratacion) 
    VALUES (1,1,'Carlos','Sanchéz','Rodriguez','2024-04-09')
    """
)

# Consultar datos 
print("\nEMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion) 
    VALUES (2,3500,'2023-05-05','2024-12-05','2024-04-09')
    """
)

# Consultar datos de estudiantes
print("\nSALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombre, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario  
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    JOIN SALARIOS ON SALARIOS.empleado_id = EMPLEADOS.id 
    """
)
for row in cursor:
    print(row)

