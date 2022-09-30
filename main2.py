import logging
from level_select import show_level_select
from game_manager import GameManager
from game_state import GameState
from telegram import Update, ChatAction 
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

updater = Updater(token="5775481865:AAETaX7SCCq5ts6u96ZDxANJRpjDyZ2m2A0", use_context=True)
dispatcher = updater.dispatcher  

def help_command_handler(update: Update, context: CallbackContext):
    with open('08b3e675949e5377fdfc830ffdaa4db7.jpg', 'rb') as file:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(update.effective_chat.id, photo=file)

help_handler = CommandHandler('help', help_command_handler)
dispatcher.add_handler(help_handler)

def start_command_handler(update: Update, context: CallbackContext):  
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!")  
    pass  

def text_message_handler(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
  
start_command_handler = CommandHandler("start", start_command_handler)  
dispatcher.add_handler(start_command_handler)  
  
text_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler) 
dispatcher.add_handler(text_handler) 

# Show game info
game_manager = GameManager("2029р.", 1)
game_manager.start()

if game_manager.game_state == GameState.START:
    print(game_manager.game_state)

 # Ask user to select game level
    level = show_level_select()
    print(f'Ви вибрали рівень: {level}')
else:
    print("Game already started.")

def message_handler(update: Update, context: CallbackContext): 
    text1 = "(лунає жіночий крик) -Ні… Ні! Не треба..! Прошу-у-у-у! Різко зіскочив, ти відкрив свої очі. (Ти)– Що за..? Тьху… знову кошмари приснились, треба піти попити води, ато в горлі пересохло…"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text1) 
    # і т .д.
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def start_handler(update: Update, context: CallbackContext):  
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!")

    context.bot.send_message(chat_id=update.effective_chat.id, text="Вставши з ліжка, ти потягнувся і повільно пішов на кухню. (Ти)– Хм.. Якесь дивне відчуття… Щось явно не те, цікаво що робить зараз Мішель? Ви підійшли до столу, взявши стакан ви підійшли до раковини та набрали води. Випили воду. (Ти)– Ммм.. Так набагато краще, ато аж говорити не міг." -1)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вставши з ліжка, ти вирішив підійти до тумбочки. На ній стояв портрет дівчини і також календар, на якому було 19 червня 2029р. (Ти)– Хех, мілашка Мішель сьогодні ж її день народження). Мені потрібно дещо їй сказати, те що я так довго приховував." -2)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Сівши, ви взяли телефон із зарядки і побачили на екрані дивне повідомлення від (-.- .-. --- -. ---) (Ти)- Що за? Хто це... Напевно знову хтось вирішив поглузувати, зараз я йому… Ти вирішив відкрити його, але відкривши його, ти засумнівівся що над тобою хтось глузує..." -3)

def handle_text_message(update: Update, context: CallbackContext):
    choice = update.message.text    
    if choice == 1:
       context.bot.send_message(chat_id=update.effective_chat.id, text=choice)
    elif choice == 2:
       context.bot.send_message(chat_id=update.effective_chat.id, text=choice)
    elif choice == 3:
       context.bot.send_message(chat_id=update.effective_chat.id, text=choice)
    else:
        context.bot.send_message("Не думаю що це хороша ідея)")

def message_handler(update: Update, context: CallbackContext): 
    choice = update.message.text

    # Start bot
updater.start_polling()