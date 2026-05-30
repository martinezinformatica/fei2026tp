#!/bin/bash

# Esperar a que la base de datos esté lista para recibir conexiones
echo "Esperando a la base de datos..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Base de datos disponible."

# 1. Crear el proyecto si la carpeta backend está vacía
if [ ! -f "manage.py" ]; then
    echo "No se encontró un proyecto Django. Creando proyecto inicial..."
    django-admin startproject mi_proyecto .
fi

# 2. Generar y aplicar migraciones
echo "Generando y aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

# 3. Crear superusuario de forma no interactiva usando variables de entorno
echo "Creando superusuario (si no existe)..."
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    python manage.py createsuperuser --no-input || echo "El superusuario ya existe o no se pudo crear."
fi

# 4. Iniciar el servidor de desarrollo de Django
echo "Arrancando el servidor de desarrollo en el puerto 8000..."
exec python manage.py runserver 0.0.0.0:8000