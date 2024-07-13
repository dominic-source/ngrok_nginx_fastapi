# Messaging System Documentation

This documentation provides an overview of the messaging system, which includes sending emails asynchronously using Celery and exposing your local development server to the internet with Ngrok. The system is built with FastAPI and uses Celery for task queue management.

## System Requirements

- Python 3.6+
- RabbitMQ (for Celery)
- Ngrok (for exposing local servers)

## Installation Guide

### Step 1: Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/dominic-source/ngrok_nginx_fastapi.git
cd ngrok_nginx_fastapi
```

### Step 2: Install Dependencies

Install the required Python packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 3: Set Up RabbitMQ

Ensure RabbitMQ is installed and running on your system as it is required by Celery as a message broker.

#### Installing RabbitMQ

- **For Ubuntu/Debian:**

  ```bash
  sudo apt-get update && sudo apt-get install rabbitmq-server
  sudo systemctl enable rabbitmq-server
  sudo systemctl start rabbitmq-server
  ```

- **For macOS (using Homebrew):**

  ```bash
  brew install rabbitmq
  brew services start rabbitmq
  ```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```plaintext
USER_EMAIL=your_email@example.com
GMAIL_THIRD_PARTY_PASSWORD=yourpassword
EMAIL_HOST=smtp.gmail.com
PORT=465
```

Replace the placeholder values with your actual email settings.

### Step 5: Start Celery Worker

Run the Celery worker from the root directory of your project.

```bash
celery -A tasks worker --loglevel=info
```

### Step 6: Start FastAPI Server

Run the FastAPI application.

```bash
uvicorn main:app --reload
```

### Step 7: Expose Local Server Using Ngrok and Nginx

- Follow the installation guide to install Nginx  and set it up [Nginx installation guide](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-plus/)

To expose your local development server to the internet, use Ngrok.

- Download and install Ngrok from [https://ngrok.com/download](https://ngrok.com/download).
- Run Ngrok to expose port 80 from our nginx reverse proxy server running on port 80.

  ```bash
  ./ngrok http 80
  ```

Ngrok will provide you with a public URL that forwards to your local server.

## Usage

After setting up the system, you can send emails by making a GET request to the FastAPI server's root endpoint (`/`) with `sendmail` and optional `talktome` query parameters.

Example:

```bash
curl http://localhost:8000/?sendmail=recipient@example.com&talktome=Your+message+here
```

Replace `localhost:8000` with your Ngrok URL if accessing from outside your local network.

## Conclusion

This system demonstrates how to set up an asynchronous email sending feature using FastAPI, Celery, and RabbitMQ, along with exposing your local server to the internet using Ngrok for testing purposes.