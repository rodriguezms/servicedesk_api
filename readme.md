# API

## Instalacion

### Crear las imagenes y ejecutar contenedores
docker-compose up -d --build

### Correr las migraciones
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

