FROM nginxinc/nginx-unprivileged:1-alpine

USER root

COPY ./default.conf.template /etc/nginx/templates/default.conf.template
COPY ./uwsgi_params /etc/nginx/uwsgi_params

RUN chmod 644 /etc/nginx/templates/default.conf.template /etc/nginx/uwsgi_params && \
    mkdir -p /vol/static && \
    chmod 755 /vol/static

USER nginx
