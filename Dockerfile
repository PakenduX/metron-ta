FROM python:3.10

WORKDIR /metron

COPY . .

RUN python -m pip install -r requirements.txt

RUN chmod u+x ./migrate_db
ENTRYPOINT ["./migrate_db"]
