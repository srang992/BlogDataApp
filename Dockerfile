FROM python:3.10.0-slim-bullseye

RUN apt-get update && \
    apt-get install -y libgtk-3-0

WORKDIR FletTutorial/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["flet", "run", "main.py"]