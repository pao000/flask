import mysql.connector, os
from dotenv import load_dotenv

load_dotenv()

config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_LOCAL_SERVER"),
    'database': os.getenv("DB_NAME"),
}

def conectar_a_db():
    try:
        # Reemplaza los valores de 'user', 'password', 'host', y 'database' con tus propios datos
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")
        return conexion
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def desconectar(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Desconexión exitosa de la base de datos.")