from typing import Final
import os
from telegram import Update
from telegram.ext import ContextTypes
from responses import Responses
import cmdontime
import cmdlate
import cmdsubmit
import cmdcorrect
import cmdlistusers

TOKEN: Final = os.getenv("TOKEN")

def _print_details(update: Update):
    chat_type = "group" if update.message.chat.type == "group" else "private"
    user_id:  str = update.message.chat.id
    print(f"ChatType: {chat_type}")
    print(f"UserId: {user_id}")

async def no_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await update.message.reply_text(Responses.PROMPT)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await update.message.reply_text(Responses.PROMPT)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    print(Responses.ERROR.format(context.error, update))

async def ontime_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await cmdontime.process_response(update, TOKEN)

async def late_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await cmdlate.process_response(update, TOKEN)

async def submit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await cmdsubmit.process_response(update, TOKEN)

async def correct_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await cmdcorrect.process_response(update, TOKEN)

async def listusers_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _print_details(update)
    await cmdlistusers.process_response(update, TOKEN)