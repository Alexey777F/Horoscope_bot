FROM python:3.9.18-bullseye
WORKDIR app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]