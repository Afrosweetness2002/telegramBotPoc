import dbusers
from telegram import Update
from bothelper import send_response

async def process_response(update: Update, token: str):
    print(update.message)
    
    users = dbusers.get_users()

    for user in users:
        response = f"{user.first_name} {user.last_name} {user.telegram_id}"
        await send_response(update, response, token)
