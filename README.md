# Sistema de Reserva de Canchas de Paddle - Backend

Este es el backend para el sistema de reservas de canchas de paddle, desarrollado con **FastAPI** como framework principal, utilizando **SQLAlchemy** para la gestión ORM y **PostgreSQL** como base de datos. Este documento proporciona una guía paso a paso para configurar y ejecutar el backend.

---

## **Requisitos previos**

Asegúrate de tener instalados los siguientes programas en tu sistema:

- Python 3.9 o superior.
- PostgreSQL.
- Git.

Además, instala un editor de texto como Visual Studio Code (recomendado).

---

## **Paso 1: Clonar el repositorio**

Clona el repositorio del proyecto en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd backend
```

---

## **Paso 2: Crear y activar el entorno virtual**

Crea un entorno virtual para gestionar las dependencias del proyecto:

```bash
python -m venv venv
```

Activa el entorno virtual:

- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

---

## **Paso 3: Instalar dependencias**

Instala las dependencias del proyecto especificadas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Las principales dependencias incluyen:

- **FastAPI:** Framework para construir APIs rápidas y modernas.
- **SQLAlchemy:** Biblioteca ORM para interactuar con bases de datos relacionales.
- **psycopg2-binary:** Controlador para conectar con PostgreSQL.
- **Pydantic:** Validación de datos.
- **python-dotenv:** Para manejar variables de entorno.

---

## **Paso 4: Configurar la base de datos**

### **Crear la base de datos en PostgreSQL**

1. Abre tu cliente PostgreSQL y crea una base de datos:

   ```sql
   CREATE DATABASE reservas;
   ```

2. Configura las credenciales de conexión en el archivo `.env` (crea este archivo en el directorio raíz si no existe):

   ```env
   DATABASE_URL=postgresql://<usuario>:<contraseña>@localhost:5432/reservas
   ```

   Reemplaza `<usuario>` y `<contraseña>` con tus credenciales de PostgreSQL.

---

## **Paso 5: Ejecutar migraciones**

El backend utiliza SQLAlchemy para gestionar el modelo de datos. Crea las tablas ejecutando el siguiente comando:

```bash
python -m app.main
```

Este paso inicializa la base de datos y crea las tablas necesarias.

---

## **Paso 6: Ejecutar el servidor**

Ejecuta el servidor de desarrollo con el siguiente comando:

```bash
uvicorn app.main:app --reload
```

Por defecto, el servidor estará disponible en `http://127.0.0.1:8000`.

---

## **Paso 7: Probar la API**

FastAPI proporciona una interfaz interactiva para probar la API:

1. Abre tu navegador y visita: `http://127.0.0.1:8000/docs`.
2. Utiliza la documentación interactiva para probar los endpoints.

---

## **Estructura del proyecto**

La estructura principal del backend es la siguiente:

```plaintext
backend/
  ├── app/
  │   ├── __init__.py          # Archivo de inicialización del módulo.
  │   ├── main.py              # Punto de entrada principal.
  │   ├── models.py            # Modelos de la base de datos.
  │   ├── schemas.py           # Validaciones de datos.
  │   ├── database.py          # Configuración de la base de datos.
  │   ├── crud.py              # Operaciones de CRUD.
  │   └── endpoints/           # Endpoints de la API.
  │       └── reservations.py  # Lógica para las reservas.
  └── .env                     # Variables de entorno.
```

---

## **Principales Endpoints**

### **Canchas**

1. **Crear cancha**
   - **Método:** POST
   - **Endpoint:** `/canchas/`
   - **Body:**
     ```json
     {
       "nombre": "Cancha 1",
       "techada": true
     }
     ```

### **Reservas**

1. **Crear reserva**
   - **Método:** POST
   - **Endpoint:** `/reservas/`
   - **Body:**
     ```json
     {
       "cancha_id": 1,
       "dia": "2024-12-20T16:00:00",
       "duracion": 2,
       "contacto_nombre": "Juan Pérez",
       "contacto_telefono": "123456789"
     }
     ```

---

## **Manejo de Errores**

El backend notifica errores de manera clara:

- Si intentas crear una reserva que se superpone con una existente, recibirás:

  ```json
  {
    "detail": "La reserva entra en conflicto con una existente."
  }
  ```

---

## **Mejores prácticas aplicadas**

1. **Separación de responsabilidades:** Cada archivo tiene una función específica (modelos, esquemas, operaciones CRUD, endpoints).
2. **Variables de entorno:** Las credenciales sensibles están gestionadas en un archivo `.env`.
3. **Validaciones robustas:** Se valida que las reservas no se solapen con otras.
4. **Documentación interactiva:** FastAPI proporciona documentación automática para los endpoints.

---

## **Próximos pasos**

- Implementar más validaciones (por ejemplo, duración mínima/máxima de reservas).
- Agregar tests automatizados.

---

## **Autor**

Ricardo Gastón Plazas

Sistema desarrollado como proyecto educativo para enseñar FastAPI y PostgreSQL.
