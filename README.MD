# Inicio de proyecto

1. Para iniciar el proyecto se debera de clonar el repositorio.

2. Se deberá de crear un archivo `.env` en la raíz del proyecto con los siguientes datos, para mayor facilidad copiar el archivo `.env.example`. A continuación la descripción de las variables de entorno:

| Variable                      | Descripción                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **DJANGO_DEBUG**              | Define si el modo de depuración de Django está activado (`True`) o desactivado (`False`).           |
| **DJANGO_SUPERUSER_USERNAME** | Nombre de usuario del superusuario creado automáticamente para el administrador de Django.          |
| **DJANGO_SUPERUSER_EMAIL**    | Correo electrónico del superusuario creado automáticamente para el administrador de Django.        |
| **DJANGO_SUPERUSER_PASSWORD** | Contraseña del superusuario creado automáticamente para el administrador de Django, si se cargan los datos de prueba, por facilidad se utilizará la misma contraseña para los mismos usuarios.                |
| **DJANGO_SECRET**             | Clave secreta utilizada por Django para criptografía y seguridad.                                  |
| **POSTGRES_HOST**             | Dirección del host del servidor de la base de datos PostgreSQL.                                    |
| **POSTGRES_PORT**             | Puerto en el que el servidor de PostgreSQL está escuchando (por defecto, `5432`).                  |
| **POSTGRES_DB**               | Nombre de la base de datos PostgreSQL utilizada por la aplicación Django.                          |
| **POSTGRES_USER**             | Nombre de usuario para conectarse a la base de datos PostgreSQL.                                   |
| **POSTGRES_PASSWORD**         | Contraseña para el usuario de la base de datos PostgreSQL.                                         |

3. Iniciar el proyecto con Docker o Virtualenv. Se recomienda utilizar *Docker* por la facilidad de uso y configuración.

# Docker

Previamente ubicarse en la carpeta del proyecto y ejecutar el siguiente comando:

```bash
docker-compose up -d
```

Esto iniciará dos contenedores, uno para la base de datos y otro para la aplicación. Automaticamente se creará un superusuario con los datos del archivo `.env`. El contenedor principal se podrá acceder por medio de la dirreccion `http://localhost:6565`

## Cargar datos de prueba

Se recomienda cargar datos de prueba para facilitar la calificación del challenge. Para cargar los datos de prueba se debe ejecutar el siguiente comando:

```bash
docker exec n5now-api /app/sample_data/load_data.sh
```

### Usuarios creados

Automáticamente se crearán los siguientes usuarios. Se debe de tomar en cuenta que se utilizará la misma contraseña de la variable `DJANGO_SUPERUSER_PASSWORD` para todos los usuarios, para simplificar la calificación del challenge.

| Username  | Email  | Password | Description |
|:------------- |:---------------:| -------------:| -------------:|
| admin         | <admin@admin.com>             | admin | Superusuario (Se crea automáticamente desde que se inicia le proyecto)   |
| oficial1      | <oficial1@example.com>        | admin | Usuario Ofical, con permisos de reportar infracciones                    |
| oficial2      | <oficial2@example.com>        | admin | Usuario Ofical, con permisos de reportar infracciones                    |

# Virtualenv

Como requisito se debe tener instalado Python 3.8 o superior y pip. Además se deberá de contar con una base de datos PostgreSQL. Para configurar la base de datos se deberá de modificar el archivo `.env` con los datos correspondientes.
Ejecutar los siguientes comandos:

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

Para crear un superusuario se debe ejecutar el siguiente comando e ingresar los datos solicitados:

```bash
python manage.py createsuperuser
```

# Acceder al proyecto

Para acceder al proyecto se debe abrir un navegador y dirigirse a la siguiente dirección:

```bash
http://localhost:8000
```

# Cargar datos de prueba

Para cargar datos de prueba se debe ejecutar el siguiente comando:

```bash
sample_data/load_data.sh
```

En ambos casos se crearán los siguientes usuarios:

Automáticamente se crearán los siguientes usuarios. Se debe de tomar en cuenta que se utilizará la misma contraseña de la variable `DJANGO_SUPERUSER_PASSWORD` para todos los usuarios, para simplificar la calificación del challenge.

| Username  | Email  | Password | Description |
|:------------- |:---------------:| -------------:| -------------:|
| oficial1      | <oficial1@example.com>        | admin | Usuario Ofical, con permisos de reportar infracciones                    |
| oficial2      | <oficial2@example.com>        | admin | Usuario Ofical, con permisos de reportar infracciones                    |


# Supuestos

1. Se asume que el usuario `admin`, quien es el superusuario, es el encargado de crear usuarios, colores, marcas y vehículos, por lo que iniciará sesion en el administrador de Django.
2. Los usuarios `oficial1` y `oficial2` son los encargados de reportar infracciones, por lo que no tendrán acceso al administrador de Django pero si los permisos necesarios para reportar infracciones.
3. Se asume que para el cliente es suficiente la interaccion que proporciona el administrador de Django para la administración de los diferentes objetos.


