#!/bin/sh

#
# Espera a que se inicialice postgres
#
if [ "$DATABASE" = "postgres" ]
then
    echo "Esperando por postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL iniciado"
fi

# Ejecuta los parametros pasados en el tag ENTRYPOINT de dockerfile
exec "$@"