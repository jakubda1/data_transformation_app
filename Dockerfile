FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "aggregator_flask_app.py", "--host=0.0.0.0"]
