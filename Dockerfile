FROM python:3.10.0-slim-bullseye

WORKDIR FletTutorial/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["flet", "run", "main.py"]