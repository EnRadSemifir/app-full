FROM nginx:1.19.0
COPY src /usr/share/nginx/html
COPY assets /usr/share/nginx/html/assets
RUN rm /etc/nginx/conf.d/default.conf
# COPY conf/nginx.dev.conf /etc/nginx/conf.d
COPY conf/nginx.prod.conf /etc/nginx/conf.d
COPY ./conf/installer.sh /tmp/installer.sh
RUN /tmp/installer.sh
RUN rm -R /tmp/installer.sh
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]