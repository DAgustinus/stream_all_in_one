# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV PYTHONPATH /code/app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7777"]
