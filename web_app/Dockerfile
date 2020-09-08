FROM nginx:1.19.0
COPY src /usr/share/nginx/html
COPY assets /usr/share/nginx/html/assets
RUN rm /etc/nginx/conf.d/default.conf
#HTTP
COPY nginx/nginx.dev.conf /etc/nginx/conf.d
EXPOSE 80
#HTTPS
# COPY nginx/nginx.prod.conf /etc/nginx/conf.d
# COPY ./nginx/installer.sh /tmp/installer.sh
# RUN /tmp/installer.sh
# RUN rm -R /tmp/installer.sh
# EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]