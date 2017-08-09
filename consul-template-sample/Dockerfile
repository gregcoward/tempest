FROM nginx:latest
MAINTAINER Gregory Coward <g.coward@f5.com>

ADD consul-template /usr/local/bin
RUN chmod a+x /usr/local/bin/consul-template
RUN mkdir /templates
ADD ping.ctmpl /templates
RUN nginx
CMD /usr/local/bin/consul-template -consul=10.0.0.129:8500 -template="/templates/ping.ctmpl:/etc/nginx/conf.d/ping.conf:service nginx reload"


