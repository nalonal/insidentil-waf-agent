FROM nginx:1.15.5

# update/upgrade your system
RUN apt-get update -y

# install required dependencies
RUN apt-get install -y git libtool \
	autoconf build-essential \
	libpcre3-dev zlib1g-dev \
	libssl-dev libxml2-dev \
	libgeoip-dev liblmdb-dev \
	libyajl-dev libcurl4-openssl-dev \
	libpcre++-dev pkgconf \
	libxslt1-dev libgd-dev automake

RUN git clone --depth 100 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity

RUN cd ModSecurity && \
	git submodule init && \
	git submodule update && \
	./build.sh && \
	./configure && \
	make && \
	make install

RUN apt-get install -y wget

RUN cd / && wget http://nginx.org/download/nginx-1.15.5.tar.gz && tar xvzf nginx-1.15.5.tar.gz && cd nginx-1.15.5

RUN git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git

RUN git clone https://github.com/openresty/headers-more-nginx-module.git headers-more-nginx-module

RUN cd nginx-1.15.5 && \
	./configure --with-compat --add-dynamic-module=/ModSecurity-nginx --add-dynamic-module=/headers-more-nginx-module && \
	make modules && \
	cp objs/ngx_http_modsecurity_module.so /usr/lib/nginx/modules && \
	cp objs/ngx_http_headers_more_filter_module.so /usr/lib/nginx/modules

RUN mkdir /etc/nginx/conf/
RUN cp /ModSecurity/unicode.mapping /etc/nginx/conf/

RUN git clone --depth 1 --branch v3.3.2 https://github.com/coreruleset/coreruleset.git /usr/src/owasp-modsecurity-crs
RUN cp -R /usr/src/owasp-modsecurity-crs/rules/ /etc/nginx/conf/

RUN mkdir /var/log/modsec/ && chmod 777 -R /var/log/modsec/

ADD nginx.conf /etc/nginx/nginx.conf
ADD modsecurity.conf /etc/nginx/conf/modsecurity.conf
ADD modsec_includes.conf /etc/nginx/conf/modsec_includes.conf
ADD crs-setup.conf /etc/nginx/conf/rules/crs-setup.conf

CMD nginx -g 'daemon off;'
