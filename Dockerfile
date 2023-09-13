FROM python:3.11

WORKDIR /opt

RUN pip install --upgrade pip

COPY docs/requirements.txt .

RUN pip install pre-commit

RUN pip install -r requirements.txt

COPY entrypoint.sh .

RUN chmod 777 entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
