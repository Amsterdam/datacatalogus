FROM python:3

MAINTAINER datapunt.ois@amsterdam.nl

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /app

RUN pip install --upgrade pip

RUN adduser --system datacatalog
RUN mkdir -p  /app/data \
    && chown datacatalog  /app/data

COPY datacatalog-core/web/requirements.txt /app/
COPY datacatalog-core/web/config-docker.yml /etc/datacatalog.yml

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY datacatalog-core/web/datacatalog/ /app/datacatalog/
COPY import /app/import/

USER datacatalog

CMD DATA_PATH=/app/data/ python /app/import/get_packages.py && python -m datacatalog.web
