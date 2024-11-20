FROM python:3.10.11-slim-buster

WORKDIR /app

COPY requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    apt-get autoremove -y

COPY . /app

CMD ["python3", "/app/twirp_server.py"]
