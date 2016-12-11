FROM ubuntu:14.04
MAINTAINER Di Chen <xxx@gmail.com>

RUN apt-get update -y && apt-get install -y libpq-dev \
                                            python-dev \
                                            ssh \
                                            python-setuptools

RUN easy_install pip

ADD requirements.txt /src/requirements.txt

RUN cd /src; pip install -r requirements.txt

ADD . /src

RUN mkdir -p /var/log/django

EXPOSE 8001

CMD ["/src/start.sh"]
