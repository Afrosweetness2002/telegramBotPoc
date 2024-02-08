from typing import Final
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from responses import Responses
from updatecmd import process_response

load_dotenv()  # load the .env file

TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME:Final = "@Farahtestbot"

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Responses.WELCOME)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Responses.PROMPT)

async def update_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_response(update, TOKEN)

# Responses
def handle_response(text:str) -> str: 
    processed = text.lower()
    
    if "hello" in processed: 
        return "Hey There!"
    
    if "how are you" in processed: 
        return "I am good, how are you"
    
    return "I do  not understand what you wrote."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    message_text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{message_text}'")

    if message_type == "group": 
        if BOT_USERNAME in message_text: 
            new_text: str = message_text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(message_text)

    print("Bot:", response)
    print(update.message.chat.id)
    chat_id = update.message.chat.id
    
    bot = telegram.Bot(TOKEN)
    async with bot:
        await bot.send_message(text=response, chat_id=chat_id)

    # await update.message.reply.text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    print(f"An error occurred: {context.error} :: {update}")

if __name__ == "__main__": 
    print("Starting Bot..")
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("update", update_command))

    # response
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors 
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)
