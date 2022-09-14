FROM python:3.9.6-alpine

WORKDIR /

COPY requirements.txt requirements.txt
RUN apk add gcc
RUN pip3 install -r requirements.txt
EXPOSE 8000

COPY . .

CMD ["uvicorn","server:app","--reload","0.0.0.0"]