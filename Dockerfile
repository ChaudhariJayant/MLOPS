from python:3.8-slim-buster

RUN apt updatae -y && apt install awsli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python3","app.py" ]