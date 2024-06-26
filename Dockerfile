FROM python:3.12.2-alpine3.19

WORKDIR /usr/src/app

RUN pip install flask prometheus-client		

COPY . .

CMD [ "python", "./app.py" ]
