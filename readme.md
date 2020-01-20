# API

## Instalacion

### Finalizar y eliminar imagenes, networks y volumenes asociados
docker-compose down -v

### Crear las imagenes y ejecutar contenedores
docker-compose up -d --build

### Correr las migraciones
docker-compose exec web python manage.py migrate --noinput

## Servicios

### Consulta una palabra y retorna los resultados

* Url: http://localhost:8080/api/v1/word_search/?word={PALABRA}

### 

* Url: http://localhost:8080/api/v1/most_wanted/