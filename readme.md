# API

## Instalacion

Finalizar y eliminar imagenes, networks y volumenes asociados:
```bash
docker-compose down -v
```

Crear las imagenes y ejecutar contenedores:
```bash
docker-compose up -d --build
```

Correr las migraciones:
```bash
docker-compose exec web python manage.py migrate --noinput
```

## Consulta una palabra y retorna los resultados:

### Request
`
curl -i -X GET http://localhost:8080/api/v1/word_search/?word=bye
`

### Response
```
HTTP/1.1 200 OK
Server: nginx/1.17.4
Date: Mon, 20 Jan 2020 04:18:01 GMT
Content-Type: application/json
Content-Length: 37
Connection: keep-alive
X-Frame-Options: DENY
X-Content-Type-Options: nosniff

{"status": "success", "result": "27"}
```

## Retorna la palabra más buscada:

### Request
`
curl -i -X GET http://localhost:8080/api/v1/most_wanted/
`

### Response
```
HTTP/1.1 200 OK
Server: nginx/1.17.4
Date: Mon, 20 Jan 2020 04:16:33 GMT
Content-Type: application/json
Content-Length: 67
Connection: keep-alive
X-Frame-Options: DENY
X-Content-Type-Options: nosniff

{"status": "success", "result": {"count": 1, "word_list": ["bye"]}}
```
