FROM python:3

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .
EXPOSE 8000

