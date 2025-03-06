# CRUD Fullstack con Vue y Django

Este repositorio contiene un proyecto Fullstack que implementa un CRUD básico utilizando **Vue** para el frontend y **Django** para el backend. Este proyecto fue desarrollado como parte de una prueba técnica.

La aplicación permite acceder a una colección de superhéroes a la que se pueden añadir más superhéroes indicando su alias, nombre real, habilidades y grupo o liga al que pertenece. También es posible editar los datos de cada héroe, eliminarlos y añadir más superpoderes y ligas mientras se está creando un nuevo superhéroe.

---

## Tecnologías Utilizadas

### Frontend
- Vue 3 (Vite)
- Vue Router
- Axios
- Tailwind CSS
- TypeScript

### Backend
- Django
- Django Rest Framework
- MySQL

- ## Instalación y Ejecución

### Backend

1. Clonar este repositorio y acceder a la carpeta backend `backend`:
    ```bash
    cd backend
    ```

2. Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows: venv\Scripts\activate
    ```

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Migrar la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Ejecutar el servidor:
    ```bash
    python manage.py runserver
    ```

### Frontend

1. Acceder al directorio `frontend`:
    ```bash
    cd frontend
    ```

2. Instalar dependencias:
    ```bash
    npm install
    ```

3. Ejecutar el servidor de desarrollo:
    ```bash
    npm run dev
    ```
    
## Versiones con las que se ha realizado el proyecto

- Python 3.13.2
- Node.js 22.14.0
- Django 5.1.6


