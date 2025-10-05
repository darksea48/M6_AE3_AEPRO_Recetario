# Proyecto Recetario y Eventos Culinarios

Este es un proyecto desarrollado con Django que funciona como un recetario de cocina y un gestor de eventos culinarios.

## Descripción

La aplicación web permite a los usuarios explorar una colección de recetas de cocina y ver una lista de próximos eventos culinarios. Además, ofrece un formulario para que los usuarios puedan añadir nuevos eventos a la lista.

Este proyecto sirve como un excelente ejemplo práctico para aprender conceptos fundamentales de Django, tales como:

-   Manejo de rutas (URLs).
-   Creación de vistas basadas en funciones.
-   Uso del sistema de plantillas de Django para renderizar contenido dinámico.
-   Procesamiento de formularios con validación de datos.
-   Gestión de datos (aunque en esta versión se manejan en memoria y de forma estática).

## Características

-   **App `recetario`**:
    -   **Página de Inicio**: Una página de bienvenida.
    -   **Listado de Recetas**: Muestra una galería de recetas con su imagen, nombre y una breve descripción.
    -   **Detalle de Receta**: Al hacer clic en una receta, se muestra una página con todos sus detalles: ingredientes, instrucciones, etc.
    -   **Listado de Eventos**: Muestra los eventos culinarios que han sido añadidos.
    -   **Formulario para Nuevos Eventos**: Una página con un formulario para registrar un nuevo evento, incluyendo validación para que la fecha no sea en el pasado.
    -   **Página de Éxito**: Confirma que un evento ha sido creado correctamente.

## Requisitos

-   Python 3.8 o superior
-   pip

## Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

1.  **Clonar el repositorio**
    ```bash
    git clone <url-del-repositorio>
    cd proyecto_recetas_ae3_abpro
    ```

2.  **Crear y activar un entorno virtual**

    -   En Windows (PowerShell):
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
        *Si encuentras un error de ejecución de scripts, ejecuta `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` y vuelve a intentarlo.*

    -   En macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instalar las dependencias**

    Asegúrate de tener un archivo `requirements.txt`. Si no lo tienes, puedes crearlo con `pip freeze > requirements.txt` después de instalar Django (`pip install Django`).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar las migraciones**

    Esto creará las tablas necesarias en la base de datos para los modelos `Receta` y `EventosCulinarios`.
    ```bash
    python manage.py migrate
    ```

5.  **Ejecutar el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```

    Ahora puedes acceder al proyecto en tu navegador visitando http://127.0.0.1:8000/.

## Estructura del Proyecto

-   `proyecto_recetas_ae3_abpro/`: Contiene la configuración principal del proyecto Django.
-   `recetario/`: La aplicación de Django que gestiona las recetas y los eventos.
-   `templates/`: Contiene las plantillas HTML del proyecto.
-   `static/`: Contiene los archivos estáticos como CSS.