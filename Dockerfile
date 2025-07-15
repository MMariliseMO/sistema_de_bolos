#Criação da imagem Docker da aplicação FastAPI

FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn peewee psycopg2-binary

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]