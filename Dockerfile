FROM python:3.13-slim
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir discord.py boto3 mcstatus python-dotenv

CMD ["python", "run.py"]