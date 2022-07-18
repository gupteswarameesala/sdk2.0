FROM python:3.8.11-alpine3.14
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["python3", "app.py"]
#CMD ["gunicorn"  , "--bind", "0.0.0.0:25000", "app:app"]