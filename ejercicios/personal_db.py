# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

# Crear tabla de DEPARTAMENTOS
try:    
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """     
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")


# Consultar datos
print("DEPARTAMENTOS:")
cursor = conn.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
    print(row)

# PLATOS:
# (1, 'Pizza', 10.99, 'Italiana')
# (2, 'Hamburguesa', 8.99, 'Americana')
# (3, 'Sushi', 12.99, 'Japonesa')
# (4, 'Ensalada', 6.99, 'Vegetariana')


# Crear tablas de CARGOS
try: 
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")


# Consultar datos 
print("\nCARGOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)

# ESTUDIANTES:
# (1, 1)
# (2, 2)
# (3, 3)
# (4, 4)

# Crear tabla de EMPLEADOS
try: 
    
    conn.execute(
        
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
        
    )

except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya existe")


# Insertar datos de EMPLEADOS
conn.execute(
    """
    INSERT INTO EMPLEADOS (departamento_id, cargo_id, nombre, apellido_paterno, apellido_materno, fecha_contratacion) 
    VALUES (1,1,'Juan','Gonzales','Perez','2023-05-15')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS (departamento_id, cargo_id, nombre, apellido_paterno, apellido_materno, fecha_contratacion) 
    VALUES (2,2,'Maria','Lopez','Martinez','2020-04-10')
    """
)

# Consultar datos 
print("\nEMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)


# PEDIDOS:
# ('Pizza', 10.99, 2, '2024-04-01')
# ('Hamburguesa', 8.99, 3, '2024-04-01')
# ('Sushi', 12.99, 1, '2024-04-02')
# ('Ensalada', 6.99, 4, '2024-04-02')    


# Crear tablas de SALARIOS
try: 
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio TEXT NOT NULL,
        fecha_fin TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id);
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya existe")

# Insertar datos de SALARIOS
conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion) 
    VALUES (1,3000,'2024-04-01','2023-05-15','2023-05-15')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion) 
    VALUES (2,3500,'2023-07-01','2024-04-30','2023-06-20')
    """
)

# Consultar datos de estudiantes
print("\nSALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)


#Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()