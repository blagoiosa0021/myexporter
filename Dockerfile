FROM python:3.12.2-alpine3.19 

WORKDIR /usr/src/myexporter/

COPY . .

RUN pip install flask prometheus-client	

CMD ["python" "app.py"]
