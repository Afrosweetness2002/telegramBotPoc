from telegram import Update, Bot
from telegram.ext import ContextTypes
from responses import Responses

async def _send_response(update: Update, response: str, token: str):
    print(response)
    bot = Bot(token)
    async with bot:
        await bot.send_message(text=response, chat_id=update.message.chat.id)

def _process_ticks(text:str) -> str:
    green_ticks = text.count(Responses.EMOJI_TICK_GREEN)

    grey_ticks = text.count(Responses.EMOJI_TICK_GREY)

    total_ticks = green_ticks + grey_ticks

    if green_ticks == 1 and grey_ticks == 0:
        return Responses.LESSON_ONTIME

    if green_ticks == 0 and grey_ticks == 1:
        return Responses.LESSON_LATE

    if total_ticks == 7:
        if green_ticks == 7:
            return Responses.LESSON_SUBMISSION_PERFECT

        if grey_ticks == 7:
            return Responses.LESSON_SUBMISSION_BAD

    if total_ticks > 7:
        # cap green ticks to 7
        # for each remaining space, add 1 to grey tick count
        return Responses.LESSON_SUBMISSION.format(green_ticks, grey_ticks)

    return Responses.LESSON_SUBMISSION.format(green_ticks, grey_ticks)

async def process_response(update: Update, token: str):
    message_type: str = update.message.chat.type
    
    print(update.message)

    if message_type == "group":
        print("Group chat detected")
    else:
        print("Private chat detected")

    message_text: str = update.message.text

    if message_text is Responses.EMOJI_TICK_GREEN:
        await _send_response(update, Responses.LESSON_COMPLETE_ONTIME, token)
        return

    if message_text is Responses.EMOJI_TICK_GREY:
        await _send_response(update, Responses.LESSON_MISSED, token)
        return
    
    response = _process_ticks(message_text)

    await _send_response(update, response, token)