FROM python:3.8

COPY requirements.txt . 
COPY ./app /app 

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--reload" ]