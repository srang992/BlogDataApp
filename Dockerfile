FROM python:3.10.0-slim-bullseye

RUN apt-get update && \
    apt-get install -y libgtk-3-0 libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-tools xvfb

WORKDIR FletTutorial/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV DISPLAY=:99
RUN Xvfb :99 -screen 0 1024x768x16 &
CMD ["xvfb-run", "--auto-servernum", "flet", "run", "main.py"]