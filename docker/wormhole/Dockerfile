# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY ./app.py /app/app.py
RUN ls
RUN pip3 install Flask
RUN pip3 install requests
ENV FLASK_APP /app/app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]