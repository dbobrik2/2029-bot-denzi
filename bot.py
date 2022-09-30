import logging
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

updater = Updater(token="5741282528:AAFPp5SZaQpF-Vr2K2PLjSaf5YGGMnWt9bM", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global state
    if state == 1:
        text = "Ви прокидаєтесь в темній кімнаті, що ви будете робити?\n1: Спати далі\n2: Йти гуляти"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        state += 1
    else:
        pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    global state
    if state == 2:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Хороший вибір")
            state = 1
            text = "Гра закінчилась. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif message == "2":
            text = "Треба знайти ключі. Де будемо шукати?\n1: Шухляда\n2: На кухні"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1
    elif state == 3:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Нічо не знайшов")
            state += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Послизнувся і вмер. Бадум тсс...")
            state += 1
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()