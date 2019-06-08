FROM python:3.6

RUN apt-get update \
    && apt-get install -y mecab \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8\
    && apt-get install -y git\
    && apt-get install -y make\
    && apt-get install -y curl\
    && apt-get install -y xz-utils\
    && apt-get install -y file\
    && apt-get install -y sudo\
    && apt-get install -y wget

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
    && cd mecab-ipadic-neologd\
    && bin/install-mecab-ipadic-neologd -n -y

RUN apt-get install -y software-properties-common vim
RUN apt-get update

RUN python3.6 -m pip install pip --upgrade

RUN pip3 install flask
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install gensim
RUN pip3 install uWSGI
RUN pip3 install mecab-python3
RUN pip install mecab-python3

ENV APP_DIR=/app/application
RUN mkdir -p $APP_DIR

ADD requirements.txt $APP_DIR
WORKDIR $APP_DIR

RUN pip install -r requirements.txt

CMD ["uwsgi","--ini","/app/application/uwsgi.ini"]

EXPOSE 5000
