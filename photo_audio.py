from email.mime import audio
from telegram import Update, ChatAction
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
 
token = "5692195960:AAEwy4UYFlIVq-vQceIyULfvR5264Xu_g5E" 
updater = Updater(token, use_context=True) 
dispatcher = updater.dispatcher 
 
def start_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!") 
 
def message_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text) 

def help_command_handler(update: Update, context: CallbackContext):
    with open('61d3b41aaaed45a6e6bbf0accb442f21.jpg', 'rb') as file:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(update.effective_chat.id, photo=file)

def cancel_command_handler(update: Update, context: CallbackContext):
    with open('Kordhell - LAND OF FIRE.mp3', 'rb') as file:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_AUDIO)
        context.bot.send_audio(update.effective_chat.id, audio=file)

help_handler = CommandHandler('help', help_command_handler)
dispatcher.add_handler(help_handler)

cancel_handler = CommandHandler('cancel', cancel_command_handler)
dispatcher.add_handler(cancel_handler)
 
start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 
 
text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler) 
dispatcher.add_handler(text_handler) 
 
# Start bot 
updater.start_polling()