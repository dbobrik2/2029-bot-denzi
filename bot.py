import logging
from tkinter import END
from tkinter.messagebox import QUESTION
from telegram import Update, ChatAction
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

START = 1
QUESTION_1 = 2
QUESTION_2 = 3
QUESTION_3 = 4
QUESTION_4 = 5
QUESTION_5 = 6
QUESTION_6 = 7
QUESTION_7 = 8
END = 9

user_states = {}

updater = Updater(token="5775481865:AAETaX7SCCq5ts6u96ZDxANJRpjDyZ2m2A0", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global user_states

    user_id = update.effective_chat.id

 #if user not in states - add him / her
    if user_id not in user_states:
        user_states[user_id] = START

    text = "(лунає жіночий крик) -Ні… Ні! Не треба..! Прошу-у-у-у! Різко зіскочив, ти відкрив свої очі. (Ти)– Що за..? Тьху… знову кошмари приснились, треба піти попити води, ато в горлі пересохло…\n1: Піти на кухню...\n2: Подивитись в телефон..."
    context.bot.send_message(chat_id = update.effective_chat.id, text=text)
    with open('спальня.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)

    if user_states[user_id] == START:
        user_states[user_id] += 1
    else:
        user_states[user_id] = 1

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text

    global user_states

    user_id = update.effective_chat.id

    if user_states[user_id] == QUESTION_1:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Вставши з ліжка, ти потягнувся і повільно пішов на кухню. (Ти)– Хм.. Якесь дивне відчуття… Щось явно не те, цікаво що робить зараз Мішель? Ви підійшли до столу, взявши стакан ви підійшли до раковини та набрали води. Випили воду. (Ти)– Ммм.. Так набагато краще, ато аж говорити не міг.")
            with open('кухня.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            user_states[user_id] = 1
            text = "Ви просто випили води і лягли дальше. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif message == "2":
            text = "Сівши, ви взяли телефон із зарядки і побачили на екрані дивне повідомлення від (-.- .-. --- -. ---) (Ти)- Що за? Хто це... Напевно знову хтось вирішив поглузувати, зараз я йому…🙄 Ти вирішив відкрити його, але відкривши його, ти засумнівівся що над тобою хтось глузує...\n1: Відкрити повідомлення...\n2: Проігнорувати"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            with open('повідомлення.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            user_states[user_id] += 1

    elif user_states[user_id] == QUESTION_2:
        if message == "1":
            text = "Відкривши повідомлення ти побачив купу незрозумілих синволів. (Ти)- Оу щось не дуже похоже на жарт, похоже на код морзе. Може я попробую це повідомлення розшифрувати.🤔\n1: Розшифрувати. \n2: Порахувати це за безглузду ідею."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            with open('морзе 1.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="(Ти)- Мда, не думаю що це щось важливе... Ліпше подрімаю...")
            with open('положив телефон.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            user_states[user_id] = 1
            text = "Ви просто проігнорували повідомлення, та лягли далі спати. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            
    elif user_states[user_id] == QUESTION_3:
        if message == "1":
            with open('морзе 2.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            text = "Прийшло ще 2 повідомлення.(розшифровка повідомлення) привіт, давай зіграєм у гру? (Ти)- В яку ще гру 🤔? Стоп, ще повідомлення... І ще...(розшифровка повідомлення) правила прості: знайти мене і за це ти получиш Мішель. (розшифровка повідомлення) не думаю що хороша ідея мене ігнорувати. \n1: Читати далі. \n2: Ігнорувати далі."
            context.bot.send_message(chat_id=update.effective_chat.id, text="(Ти)- Мішель... Що за хрінь... Я йому невірю... Так і напишу.")
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] = 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="(Ти)- Що за маячня.")
            with open('положив телефон.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            user_states[user_id] += 1
            text = "Ви просто проігнорували повідомлення, та лягли далі спати. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                
    elif user_states[user_id] == QUESTION_4:
        if message == "1":
            with open('морзе 3.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            text = "(Ти)- Я написав йому що ніодному його слову не вірю... Тоді він прислав фото... Там була Мішель... Чому всі хочуть її в мене відібрати... Тільки все почало потрохи налагоджуватись.. мені потрібно зось зробити. \n1: Відповісти йому та зіграти у гру. \n2: Попросити зробити щось інше."
            context.bot.send_message(chat_id=update.effective_chat.id, text="(Ти)- Давай перше завдання. Написав я йому.")
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="(Ти)- ...")
            with open('положив телефон.jpg', 'rb') as file:
                context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
                context.bot.send_photo(update.effective_chat.id, photo=file)
            user_states[user_id] = 1
            text = "Він не захотів іти тобі на уступки, ти показав йому що ти слабкий, тому маньяк вбив Мішель, ти втратив смисл життя. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)        
    
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()