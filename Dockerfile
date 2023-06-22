FROM python:3.9

WORKDIR /app

COPY ./static /app/static

COPY ./templates /app/templates

COPY ./src /app/src

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# run fastapi code 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]