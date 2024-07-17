# use python image as the base image
FROM python:latest

# Set the working directory
WORKDIR /app

COPY ..

RUN pip install -r requirements.txt

EXPOSE 8000

RUN celery -A tasks worker --loglevel=info --detach

CMD ["fastapi dev &> /dev/null &"]
