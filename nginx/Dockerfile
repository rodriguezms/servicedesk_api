# Obtiene la imagen oficial de nginx, SO alpine
FROM nginx:1.17.4-alpine

# Elimina la configuracion por default 
RUN rm /etc/nginx/conf.d/default.conf

# Copia el archivo de config para nginx del proyecto
COPY nginx.conf /etc/nginx/conf.d