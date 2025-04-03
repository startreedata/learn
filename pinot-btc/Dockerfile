FROM python:3.12-slim

WORKDIR /opt/pinot-kafka

RUN pip install poetry
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "ticker.py"]