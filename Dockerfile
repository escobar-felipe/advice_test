FROM python:3.10.2 

WORKDIR /advice_test

COPY /carford /carford
COPY ./requirements.txt /advice_test

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    
COPY . /advice_test

CMD ["gunicorn", "carford.wsgi:app","--bind=0.0.0.0:8000"]