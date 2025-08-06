FROM python:3.9.19-slim-bullseye
RUN apt update
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
