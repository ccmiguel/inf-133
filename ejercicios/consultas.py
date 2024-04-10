
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
    VALUES (2,2,'Maria','Lopez','Martinez','Senior','2020-04-10')
    """
)
# Insertar datos de SALARIOS
conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1,3000,'2024-04-01','2023-05-15','2023-05-15')
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (2,3500,'2023-07-01','2024-04-30','2023-06-20')
    """
)



# Insertar datos de CARGOS
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Gerente de Ventas','Senior','2020-04-10')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Analista de Marketing','Junior','2020-04-11')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Representante de Ventas','Junior','2020-04-12')
    """
)

    
# Insertar datos de departamento
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Ventas','2020-04-10')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Marketing','2020-04-11')
    """
)