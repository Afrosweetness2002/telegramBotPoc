from telegram import Update
from responses import Responses
from bothelper import send_response

def _process_ticks(text:str) -> str:
    green_ticks = text.count(Responses.EMOJI_TICK_GREEN)

    grey_ticks = text.count(Responses.EMOJI_TICK_GREY)

    total_ticks = green_ticks + grey_ticks
    
    if total_ticks == 0:
        return Responses.LESSON_SUBMISSION_PROMPT_FULL

    if total_ticks > 7:
        return Responses.LESSON_SUBMISSION_MAX

    if green_ticks == 7:
        return Responses.LESSON_SUBMISSION_PERFECT

    if grey_ticks == 7:
        return Responses.LESSON_SUBMISSION_BAD

    return Responses.LESSON_SUBMISSION.format(green_ticks, grey_ticks)

async def process_response(update: Update, token: str):
    print(update.message)

    message_text: str = update.message.text
    
    response = _process_ticks(message_text)

    await send_response(update, response, token)