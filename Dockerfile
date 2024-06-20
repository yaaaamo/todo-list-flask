
FROM python:3.8

WORKDIR /app

ADD . /app


RUN pip install --no-cache-dir -r requirements.txt


ENV PORT = 5001

EXPOSE 5001


CMD ["python", "app.py"]
