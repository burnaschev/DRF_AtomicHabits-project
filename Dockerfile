FROM python:3.10

WORKDIR /Atomic

RUN pip install --upgrade pip

COPY requirements.txt /Atomic

RUN pip install -r requirements.txt

COPY . .
