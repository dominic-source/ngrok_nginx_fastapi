# use python image as the base image
FROM python:latest

# Set the working directory
WORKDIR /app

COPY ..

RUN pip install -r requirements.txt

RUN chmod +x ngrok-entrypoint.sh

EXPOSE 8000

RUN celery -A tasks worker --loglevel=info --detach

CMD ["sh", "-c", "fastapi dev &> /dev/null &"]
