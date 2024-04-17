# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

# Consultar datos de Personal JOIN
print("\nPERSONAL: EJERCICIOS_1")

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombre, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario  
    FROM EMPLEADOS
    JOIN SALARIOS ON SALARIOS.empleado_id = EMPLEADOS.id 
    """
)
for row in cursor:
    print(row)


# Consultar datos de Personal JOIN
print("\nPERSONAL: EJERCICIOS_2")

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



# Consultar datos de Personal JOIN
print("\nPERSONAL: EJERCICIOS_3")

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

