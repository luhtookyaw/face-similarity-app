FROM python:latest

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY ./app /app 

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:app"]