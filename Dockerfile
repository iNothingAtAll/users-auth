# Imagen base
FROM python:3.13.12-slim


# Establece el directorio de trabajo
WORKDIR /usr/src/app


COPY . .


# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
