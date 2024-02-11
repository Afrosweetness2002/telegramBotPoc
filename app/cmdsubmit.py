from telegram import Update
from responses import Responses
from bothelper import send_response

def _process_ticks(text:str) -> str:
    green_ticks = text.count(Responses.EMOJI_TICK_GREEN)

    grey_ticks = text.count(Responses.EMOJI_TICK_GREY)

    total_ticks = green_ticks + grey_ticks
    
    if total_ticks == 7:
        if green_ticks == 7:
            return Responses.LESSON_SUBMISSION_PERFECT

        if grey_ticks > 3:
            return Responses.LESSON_SUBMISSION_MOST_BAD
        
        if grey_ticks == 7:
            return Responses.LESSON_SUBMISSION_BAD

    if total_ticks > 7:
        # cap green ticks to 7
        # for each remaining space, add 1 to grey tick count
        return Responses.LESSON_SUBMISSION.format(green_ticks, grey_ticks)

    return Responses.LESSON_SUBMISSION.format(green_ticks, grey_ticks)

async def process_response(update: Update, token: str):
    print(update.message)

    message_text: str = update.message.text
    
    response = _process_ticks(message_text)

    await send_response(update, response, token)