FROM nginx:latest
MAINTAINER Gregory Coward <g.coward@f5.com>

RUN wget https://releases.hashicorp.com/consul-template/0.12.0/consul-template_0.12.0_linux_amd64.zip
RUN unzip -d /usr/local/bin consul-template_0.12.0_linux_amd64.zip
RUN chmod a+x /usr/local/bin/consul-template
RUN mkdir /templates
ADD ping.ctmpl /templates
RUN nginx /usr/local/bin/consul-template -consul 10.0.0.129:8500 -template "/templates/ping.ctmpl:/etc/nginx/conf.d/ping.conf:service nginx reload" -pid-file /var/run/consul-template.pid -log-level warn


