# users-auth
Esta es una API basica para autenticar usuarios de una base de datos SQL. Está hecha en Python y puede ser lanzada con Docker.


## Base de datos
Para el correcto funcionamiento de la API, es necesario que exista una base de datos SQL. La API usa las variables de entorno en `.env` para hacer la conexion.


## Ejecución con Docker

La imagen de la aplicación está disponible en GitHub Container Registry. Puedes descargar y ejecutar la aplicación de la siguiente manera:

### Descargar la imagen
```bash
docker pull ghcr.io/inothingatall/users-auth:latest
```

### Ejecutar el contenedor
```bash
docker run -p 8000:8000 \
  --env-file .env \
  ghcr.io/inothingatall/users-auth:latest
```

Asegúrate de que el archivo `.env` en tu máquina local contiene todas las variables de entorno necesarias para la conexión a la base de datos.