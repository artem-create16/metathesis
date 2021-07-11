FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY requirements-dev.txt ./

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]