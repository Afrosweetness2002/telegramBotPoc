from telegram import Update
from responses import Responses
from bothelper import send_response

async def process_response(update: Update, token: str):    
    print(update.message)
    await send_response(update, Responses.LESSON_ONTIME, token)