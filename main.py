from fastapi import FastAPI, HTTPException
from tasks import send_email_task
import logging
from datetime import datetime

app = FastAPI()

# Configure logging
logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.DEBUG, format='%(message)s - %(asctime)s')

@app.get("/")
async def send_mail(sendmail: str, talktome: str = None):
    if sendmail:
        # Queue the email sending task
        send_email_task.delay(sendmail, talktome)
        if talktome:
            logging.debug(f"Current time logged at")
        return {"message": "Mail has been added to queue"}
    else:
        raise HTTPException(status_code=400, detail="sendmail parameter is required")
