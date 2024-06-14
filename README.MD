# Infractions Challenge

- [Iniciar proyecto con docker](#iniciar-challenge-con-docker)
- [Documentación del sistema](#documentación-del-sistema)

## Iniciar challenge con Docker

1. Prerequisitos
    1.1 Docker

2. Clonar el repositorio en la carpeta deseada.

3. Crear un archivo `.env` en la raíz del proyecto con los siguientes datos, para mayor facilidad copiar el archivo `.env.example`. A continuación la descripción de las variables de entorno:

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

Ejecutar el siguiente comando:

```bash
docker-compose up -d
```

Se recomienda cargar datos de prueba para facilitar la calificación del challenge. Ejecutar el siguiente comando:

```bash
docker exec n5now-api /app/sample_data/load_data.sh
```

Esto iniciará dos contenedores, uno para la base de datos y otro para la aplicación. Automaticamente se creará un superusuario con los datos del archivo `.env`. El contenedor principal se podrá acceder por medio de la dirreccion `http://localhost:6565`

### Datos de prueba creados

#### Usuarios

Automáticamente se crearán los siguientes usuarios. Se debe de tomar en cuenta que se utilizará la misma contraseña de la variable `DJANGO_SUPERUSER_PASSWORD` para todos los usuarios, para simplificar la calificación del challenge.

| Username  | Email  | Password | Description |
|:------------- |:---------------:| -------------:| -------------:|
| admin         | <admin@admin.com>             | admin | Superusuario (Se crea automáticamente desde que se inicia le proyecto)   |
| oficial1      | <oficial1@example.com>        | admin | Usuario Oficial, con permisos de reportar infracciones                    |
| oficial2      | <oficial2@example.com>        | admin | Usuario Oficial, con permisos de reportar infracciones                    |

## Documentación del sistema

### Menu principal

Dentro del menú principal se mostraran las siguientes opciones

![Menu principal](docs/images/options.png)

#### Iniciar sesión como administrador

Utilizar el usuario username: `admin` y password: `admin`. Se mostrará el menú principal de administrador, en donde se podrán administrar Marcas, Colores, Oficiales, Vehículos, Infracciones y Personas.
![Menu principal](docs/images/admin.png)

#### Consultar infracciones

Se mostrará un formulario para consultar las infracciones de una persona. Se debe de ingresar el correo electrónico de la persona y se mostrarán los vehículos de las personas y las ifracciones que ha cometido. Se podrán utilizar los siguientes usuarios de prueba para consultar las infracciones:
    - `juan.perez@example.com`
    - `maria.lopez@example.com`
    - `carlos.gomez@example.com`

![Menu principal](docs/images/infractions.png)

#### Crear infracción

- Iniciar sesion con el usuario `oficial1` o `oficial2` con password `admin`.
- Se mostrará el token generado al iniciar sesion via JWT, además se activará un formulario para reportar una infracción. Se debe de ingresar la placa del vehículo, la fecha de la infracción y la descripción de la infracción. Se podrán utilizar los siguientes vehículos de prueba para reportar infracciones:
  - `IJK123` Se reflejará en las infracciones del usuario `juan.perez@example.com`
  - `LMN456` Se reflejará en las infracciones del usuario `maria.lopez@example.com`
  - `OPQ789` Se reflejará en las infracciones del usuario `carlos.gomez@example.com`

![Menu principal](docs/images/create_infraction.png)
