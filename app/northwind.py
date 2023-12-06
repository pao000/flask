from app.conexiones.conexion import conectar_a_db, desconectar

def obtener_tabla(table_name):
    connection = conectar_a_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name}")  
    data = cursor.fetchall()
    cursor.close()
    desconectar(connection)
    return data


