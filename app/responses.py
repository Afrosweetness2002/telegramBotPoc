class Responses:
    WELCOME = "Hello! Thanks for chatting with me! I am your khair assistant!"
    PROMPT = "I am your khair assistant! Please use a command to submit your lessons!"
    ERROR = "An error occurred: {0} :: {1}"
    EMOJI_TICK_GREEN = "\u2705"
    EMOJI_TICK_GREY = "\u2611\uFE0F"
    EMOJI_WARNING = "\u260A0"
    EMOJI_INFORMATION = "\u2139"
    LESSON_ONTIME = "You completed your lesson on time! Allahumma baarik! " + EMOJI_TICK_GREEN
    LESSON_LATE = "You completed your lesson late, do better next time."
    LESSON_CORRECTION = "Lessons submitted: {0} on time and {1} late"
    LESSON_SUBMISSION = "Lessons submitted: {0} on time and {1} late"
    LESSON_SUBMISSION_PROMPT = "Please enter the newly completed lessons you want to add"
    LESSON_SUBMISSION_PROMPT_FULL = "Please enter the full list of lessons you've completed"
    LESSON_SUBMISSION_PERFECT = "You completed all lessons on time! Allahumma baarik! " + EMOJI_TICK_GREEN
    LESSON_SUBMISSION_MOST_BAD = "You completed most your lessons late. Do better next week."
    LESSON_SUBMISSION_BAD = "You failed to complete any lessons on time. We need to talk."
    LESSON_SUBMISSION_MAX = "You've entered more than 7 lessons, please check your submission. " + EMOJI_WARNING + EMOJI_INFORMATION