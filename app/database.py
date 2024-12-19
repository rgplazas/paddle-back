# Importar las librerías necesarias
from sqlalchemy import create_engine  # Permite crear una conexión a la base de datos
from sqlalchemy.orm import sessionmaker, declarative_base  # Herramientas para trabajar con ORM y definir modelos
import os  # Módulo para interactuar con el sistema operativo
from dotenv import load_dotenv  # Librería para cargar variables de entorno desde un archivo .env

# Cargar variables de entorno desde el archivo .env
load_dotenv()  # Esta función busca un archivo .env en el directorio actual y carga las variables de entorno definidas en él.

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")  # Extrae el valor de la variable DATABASE_URL definida en el archivo .env

# Verificar que DATABASE_URL esté configurada
if not DATABASE_URL:
    raise ValueError("La variable DATABASE_URL no está configurada en el archivo .env")
    # Si no se encuentra la URL, se lanza un error informando que falta configurar esta variable.

# Configuración de SQLAlchemy
engine = create_engine(DATABASE_URL)  # Crea una instancia del motor de SQLAlchemy que se conecta a la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# sessionmaker configura una clase para crear sesiones de base de datos:
# - autocommit=False: No se ejecutan cambios automáticamente.
# - autoflush=False: No se ejecutan automáticamente las consultas antes de tiempo.
# - bind=engine: Asocia las sesiones al motor (engine) creado.

Base = declarative_base()  
# declarative_base se utiliza para definir las clases del modelo ORM. Todas las tablas de la base de datos se heredan de esta clase.


# Prueba de conexión
'''
def test_connection():
    try:
        with engine.connect() as connection:  # Se intenta establecer una conexión temporal con la base de datos.
            print("Conexión exitosa a la base de datos.")  # Mensaje si la conexión fue exitosa.
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")  # Mensaje de error si falla la conexión.

if __name__ == "__main__":  # Este bloque asegura que el código solo se ejecute cuando se ejecuta el script directamente.
    test_connection()  # Se llama a la función de prueba de conexión.
'''