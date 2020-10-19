FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /landshark
WORKDIR /landshark
COPY requirements.txt /landshark/
RUN pip install -r requirements.txt
COPY . /landshark/