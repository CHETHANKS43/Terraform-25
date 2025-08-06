FROM python:3.14.0b2-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]