FROM python:3.8

WORKDIR /usr/src/app
ADD . /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uwsgi", "app.ini"]
