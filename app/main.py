from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
import cmdfactory;

# REQUIRED: Load the .env file
load_dotenv()

# REQUIRED: Application entry point
if __name__ == "__main__": 
    print("Starting Bot..")
    app = Application.builder().token(os.getenv("TOKEN")).build()

    # General handlers
    app.add_handler(CommandHandler("help", cmdfactory.help_command))

    # Lesson command handlers
    app.add_handler(CommandHandler("ontime", cmdfactory.ontime_command))
    app.add_handler(CommandHandler("late", cmdfactory.late_command))
    app.add_handler(CommandHandler("submit", cmdfactory.submit_command))
    app.add_handler(CommandHandler("correct", cmdfactory.correct_command))
    app.add_handler(CommandHandler("listusers", cmdfactory.listusers_command))

    # Fallback (note: order matters, this should be added last)
    app.add_handler(MessageHandler(filters.TEXT, cmdfactory.no_command))

    # Error handler
    app.add_error_handler(cmdfactory.error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)
