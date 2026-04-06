FROM python:3.11

WORKDIR /app

COPY ./app ./app
COPY requirement.txt .

RUN pip install -r requirement.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
