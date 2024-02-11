from telegram import Update, Bot

async def send_response(update: Update, response: str, token: str):
    print(f"Sending response: {response}")
    bot = Bot(token)
    async with bot:
        await bot.send_message(text=response, chat_id=update.message.chat.id)