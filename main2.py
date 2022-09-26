from level_select import show_level_select
from game_manager import GameManager
from game_state import GameState
from telegram import Update 
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext 

def intro():
    """Function ssks for user name to play game."""

    print("Введіть ім'я:")
    name = input()
    print(f'"Привіт: {name}')

token = "5775481865:AAETaX7SCCq5ts6u96ZDxANJRpjDyZ2m2A0" 
updater = Updater(token, use_context=True)  
dispatcher = updater.dispatcher  
  
def start_handler(update: Update, context: CallbackContext):  
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!")  
    pass  
 
def message_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text) 
  
start_command_handler = CommandHandler("start", start_handler)  
dispatcher.add_handler(start_command_handler)  
  
text_handler = MessageHandler(Filters.text & ~Filters.comand, message_handler) 
dispatcher.add_handler(text_handler) 
 
# Start bot  
updater.start_polling()

# Show game info
game_manager = GameManager("2029р.", 1)
game_manager.start()

if game_manager.game_state == GameState.START:
    print(game_manager.game_state)

# Show user intro
    intro()

 # Ask user to select game level
    level = show_level_select()
    print(f'Ви вибрали рівень: {level}')
else:
    print("Game already started.")

print("(лунає жіночий крик) -Ні… Ні! Не треба..! Прошу-у-у-у! Різко зіскочив, ти відкрив свої очі. (Ти)– Що за..? Тьху… знову кошмари приснились, треба піти попити води, ато в горлі пересохло…")
print("Піти на кухню (1)")
print("Підійти до тумбочки (2)")
print("Подивитись в телефон (3)")
choice = input()
if choice == 1:
    print("Вставши з ліжка, ти потягнувся і повільно пішов на кухню. (Ти)– Хм.. Якесь дивне відчуття… Щось явно не те, цікаво що робить зараз Мішель? Ви підійшли до столу, взявши стакан ви підійшли до раковини та набрали води. Випили воду. (Ти)– Ммм.. Так набагато краще, ато аж говорити не міг.")
elif choice == 2:
    print("Вставши з ліжка, ти вирішив підійти до тумбочки. На ній стояв портрет дівчини і також календар, на якому було 19 червня 2029р. (Ти)– Хех, мілашка Мішель сьогодні ж її день народження). Мені потрібно дещо їй сказати, те що я так довго приховував.")
elif choice == 3:
    print("Сівши, ви взяли телефон із зарядки і побачили на екрані дивне повідомлення від (-.- .-. --- -. ---) (Ти)- Що за? Хто це... Напевно знову хтось вирішив поглузувати, зараз я йому… Ти вирішив відкрити його, але відкривши його, ти засумнівівся що над тобою хтось глузує...")
else:
    print("Не думаю що це хороша ідея)")