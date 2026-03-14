# users-auth
Esta es una API basica para autenticar usuarios de una base de datos SQL. Está hecha en Python y puede ser lanzada con Docker.


## Base de datos
Para el correcto funcionamiento de la API, es necesario que exista una base de datos SQL. La API usa las variables de entorno en `.env` para hacer la conexion.


## Ejecución con Docker
La imagen de la API está disponible en GitHub Container Registry y se puedes descargar individualmente usando:


### Descargar
```bash
docker pull ghcr.io/inothingatall/users-auth:latest
```


## Docker Compose
Se implementó Docker Compose para desplegar una base de datos SQL y hacer una conexión simulada con el fin de probar el funcionamiento de la API.


### Ejecutar
```bash
docker-compose up -d
```

### Eliminar
```bash
docker-compose down -v
```