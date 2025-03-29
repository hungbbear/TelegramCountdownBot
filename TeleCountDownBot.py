from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from datetime import datetime

def remaining_time_from_gregorian(year, month, day, hour, minute, second):
    target_gregorian_datetime = datetime(year, month, day, hour, minute, second)

    current_gregorian_datetime = datetime.now()

    remaining_time = target_gregorian_datetime - current_gregorian_datetime

    remaining_days = remaining_time.days
    remaining_hours, remainder = divmod(remaining_time.seconds, 3600)
    remaining_minutes, remaining_seconds = divmod(remainder, 60)

    return remaining_days, remaining_hours, remaining_minutes, remaining_seconds

# Your Gregorian Date time you want to count here 
future_gregorian_year = 2024
future_gregorian_month = 3
future_gregorian_day = 7
future_gregorian_hour = 9
future_gregorian_minute = 0
future_gregorian_second = 0

remaining_days, remaining_hours, remaining_minutes, remaining_seconds = remaining_time_from_gregorian(
    future_gregorian_year, future_gregorian_month, future_gregorian_day,
    future_gregorian_hour, future_gregorian_minute, future_gregorian_second
)


def msg(remaining_days, remaining_hours, remaining_minutes, remaining_seconds):
    
    msg = f"🎈Remaining time until the final competition: {remaining_days} days, {remaining_hours} hours, {remaining_minutes} minutes, {remaining_seconds} seconds\n"
    return msg


TOKEN = "<YOUR_BOT_TOKEN>"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Send /time to get day count message.')

def time(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg(*remaining_time_from_gregorian(
    future_gregorian_year, future_gregorian_month, future_gregorian_day,
    future_gregorian_hour, future_gregorian_minute, future_gregorian_second
)))

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("time", time))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

