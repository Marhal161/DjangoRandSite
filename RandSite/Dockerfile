FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR ./RandSite

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt