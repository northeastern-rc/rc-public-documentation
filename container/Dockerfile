FROM python:3.11

WORKDIR /opt

COPY /docs/requirements.txt .

RUN pip install --upgrade pip && \
    pip install pre-commit && \
    pip install -r requirements.txt

COPY container/entrypoint.sh .

RUN chmod 777 entrypoint.sh

WORKDIR /rtd

ENTRYPOINT ["/opt/entrypoint.sh"]
