FROM python:3.8

LABEL maintainer="Tutu Godfrey"

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py" ]
