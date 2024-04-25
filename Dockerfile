FROM python:3.9

WORKDIR /src

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
