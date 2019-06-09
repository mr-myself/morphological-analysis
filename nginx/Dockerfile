FROM nginx
RUN mkdir -p /etc/nginx
COPY ./nginx.conf /etc/nginx/
CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]

EXPOSE 80
EXPOSE 443
