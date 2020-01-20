###########
# BUILDER #
###########

FROM python:3.8.0-alpine as builder

# Setea el directorio de trabajo
WORKDIR /usr/src/app

# No escribe los archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# No buffer de stdout y stderr
ENV PYTHONUNBUFFERED 1

# Instala las dependencias de Postgresql
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Actualiza pip
RUN pip install --upgrade pip
# Instala linter
RUN pip install flake8
# Copia el proyecto
COPY . .
# Corre el linter al proyecto
RUN flake8 --ignore=E501,F401 .

# Genera el archivo wheel para distribucion
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

FROM python:3.8.0-alpine

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

# Setea el directorio de trabajo
WORKDIR $APP_HOME

# Crea el directorio del usuario 'app'
RUN mkdir -p $APP_HOME

# Crea el usuario 'app'
RUN addgroup -S app && adduser -S app -G app

# Instala dependencias
RUN apk update && apk add libpq

# Se trae las dependencias de la imagen que construye la app
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

# Actualiza pip
RUN pip install --upgrade pip
# Instala las librerias generadas
RUN pip install --no-cache /wheels/*

# Copia el proyecto
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# Cambia al usuario 'app'
USER app

# Ejecuta entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]


CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "invGateProject.wsgi:application"]