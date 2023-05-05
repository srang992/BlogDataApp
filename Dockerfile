FROM python:3.10.0-slim-bullseye

WORKDIR /BlogApp

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "./main.py"]