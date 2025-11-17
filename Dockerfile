FROM python:3.9-buster

# Install awscli with pip
RUN pip install awscli
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]