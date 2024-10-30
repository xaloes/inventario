import sqlite3

# Conectar a la base de datos (si no existe, se creará)
conexion = sqlite3.connect('db.sqlite3')
print("conectado a la bbdd")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla para el ejemplo si no existe


# Insertar un registro en la tabla
cursor.execute('''
INSERT INTO gestion_categoria (id, nombre)
VALUES (?, ?)
''', ("1", "electronica"))



print("insert lanzado")
# Confirmar los cambios
conexion.commit()
print("insert confirmado")
# Cerrar la conexión
conexion.close()
print("Cerrado")


