FROM python:3.6.8-slim

ENV LANG C.UTF-8
WORKDIR /app
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
