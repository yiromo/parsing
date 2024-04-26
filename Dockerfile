FROM python:3.9

WORKDIR /src

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libzbar0 libzbar-dev

CMD ["python", "./src/main.py"]
