FROM python:3.10.0-slim-bullseye

WORKDIR FletTutorial/

COPY requirements.txt .

RUN apt-get update && sudo apt-get install libgtk-3-0

RUN pip install -r requirements.txt

COPY . .

CMD ["flet", "run", "main.py"]