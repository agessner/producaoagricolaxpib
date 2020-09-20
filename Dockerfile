FROM python:3.7

WORKDIR /app

COPY fifaeng-c8403084b672.json googlecredentials.json
ENV GOOGLE_APPLICATION_CREDENTIALS /app/googlecredentials.json

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy && \
    chmod +x cloud_sql_proxy && \
    mkdir /cloudsql && \
    chown -R "$USER" /cloudsql
ENV DB_SOCKET_DIR /cloudsql

COPY main.py main.py
COPY app/ app/

COPY entrypoint.sh entrypoint.sh
RUN chmod 755 entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]