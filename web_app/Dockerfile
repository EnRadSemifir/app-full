FROM nginx:1.19.0
COPY src /usr/share/nginx/html
COPY assets /usr/share/nginx/html/assets
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.dev.conf /etc/nginx/conf.d
RUN apt-get update && apt-get install apache2-utils -y
RUN apt-get install certbot python-certbot-nginx -y
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]