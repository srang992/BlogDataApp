FROM python:3.10.0-slim-bullseye

WORKDIR FletTutorial/

COPY requirements.txt .

RUN apt-get update && apt-get install -y libstdc++6

RUN pip install -r requirements.txt

COPY . .

CMD ["flet", "run", "main.py"]