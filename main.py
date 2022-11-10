import telebot, json, difflib, random, datetime
import inline
#####################################
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode="html")
#####################################
def config_open():
    global database, swear_db
    with open('database.json', encoding='utf-8') as f:
        database = json.load(f)
    with open('swear.json', encoding='utf-8') as f:
        swear_db = json.load(f)

def config_save():
    global database
    with open('database.json', 'w', encoding="utf-8") as f:
        json.dump(database, f, indent=4, ensure_ascii=False)
#####################################
@bot.message_handler(content_types=['text'])
def add_word(message):
    print("[INPUT] сообщение получено!")
    config_open()
    if message.reply_to_message != None and message.reply_to_message.from_user.id == 5516081643 or message.chat.id == message.from_user.id:
        bot.reply_to(message, random.choice(database['messages']))
    else:
        for i in swear_db:
            if (i in message.text) == True or (difflib.SequenceMatcher(None, (message.text).lower(), i.lower()).ratio()) > 0.90:
                print(f"[MESSAGE] обнаружены запрещенные символы/слова! ({i})")
                return
        if (message.text.lower() in database['messages']) == False:
            print("[MESSAGE] сообщение добавлено!")
            database['messages'].append(message.text.lower())
            config_save()
#####################################
#####################################
@bot.callback_query_handler(func=lambda call: True)
def rater(call):
    config_open()
    print(f"[RATE] {call.data}")
    if call.data.startswith('rate '):
        split_data = call.data.split()
        database['music'][int(split_data[1])] = database['music'][int(split_data[1])] + 1
        config_save()
        bot.send_message(call.from_user.id, f"{call.from_user.first_name} ({call.from_user.username}) поставил ⭐️") 
#####################################
@bot.inline_handler(func=lambda query: len(query.query) > 0)
def quyrer(query):
    user_status = bot.get_chat_member(-1001890972108, query.from_user.id).status
    if user_status == 'member' or user_status == 'creator' or user_status == 'administrator':
        
        bot.answer_inline_query(query.id, inline.get_list(), cache_time=0 ,is_personal=True)
    
    else:
        result = []
        result.append(telebot.types.InlineQueryResultArticle(
                thumb_url="https://i.ibb.co/MCGx6bH/photo-2022-11-04-11-48-40.jpg",
                id=1, title="Упс...", description="Что бы использовать инлайны этого бота подпишись на @bsddatamines_chat",
                input_message_content=telebot.types.InputTextMessageContent(message_text="Что бы использовать инлайны этого бота зайди в @bsddatamines_chat")))
        bot.answer_inline_query(query.id, result, cache_time=0 ,is_personal=True)
#####################################
while True:
    print("...")
    try:
        print(f"===== BOT STARTED =====\ntime: {datetime.now()}\ntoken: {TOKEN}\n")
        bot.remove_webhook()
        bot.polling(none_stop=True)
    except Exception as err:
        print(f"[Error]: {err}\n")
        print("===== BOT STOPPED =====\n\n")