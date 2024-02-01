from typing import Final
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()  # load the .env file


TOKEN: Final = os.getenv("TOKEN")


BOT_USERNAME:Final = "@Farahtestbot"


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am your khair assistant!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am your khair assistant! Please type something so I can respond')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom Command!')


# Responses
def handle_response(text:str) -> str: 
    processed = text.lower()
    
    if "hello" in processed: 
        return "Hey There!"
    
    if "how are you" in processed: 
        return "I am good, how are you"
    
    return "I do  not understand what you wrote. "


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}' ")

    if message_type == "group": 
        if BOT_USERNAME in text: 
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else: 
            return 
    else: 
        response: str = handle_response(text)

    print("Bot:", response)
    print(update.message.chat.id)
    chat_id = update.message.chat.id


    bot = telegram.Bot(TOKEN)
    async with bot:
        await bot.send_message(text=response, chat_id=chat_id)

    # await update.message.reply.text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    print(f"Update {update} caused error {context.error}")




if __name__ == "__main__": 
    print("Starting Bot..")
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))


    # response
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors 
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)

