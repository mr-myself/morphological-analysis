FROM nginx
RUN mkdir -p /etc/nginx
ADD ./nginx.conf /etc/nginx/
CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
