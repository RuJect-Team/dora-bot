import json, telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_list():
    result = []
    with open('database.json', encoding='utf-8') as f:
        database = json.load(f)
    
    result.append(
            telebot.types.InlineQueryResultAudio(
            id=0, title="Дорадура", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="⭐️", callback_data=f"rate 0")),
            audio_url="https://mp3uks.ru/mp3/files/dora-doradura-mp3.mp3",
            caption=f"⭐️: {database['music'][0]} \nЗакрываю дверь квартиры\nОтключаю все мобилы\nНедоступна для дебилов\nПотому что я влюбилась..."
            ))
    result.append(
            telebot.types.InlineQueryResultAudio(
            id=1, title="Втюрилась", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="⭐️", callback_data=f"rate 1")),
            audio_url="https://mp3uks.ru/mp3/files/dora-vtyurilas-mp3.mp3",
            caption=f"⭐️: {database['music'][1]} \nПривет\nНо ты проходишь мимо\nЯ спрятала улыбку\nМне важно, чтобы ты узнал\nСекрет, секрет..."
            ))
    result.append(
            telebot.types.InlineQueryResultAudio(
            id=2, title="Кьют-рок", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="⭐️", callback_data=f"rate 2")),
            audio_url="https://mp3uks.ru/mp3/files/dora-kyut-rok-mp3.mp3",
            caption=f"⭐️: {database['music'][2]} \nЯ иду на фестиваль ведь обещала всем своим подругам\nВ очереди час плюс на входе обшмонали грубо\nЯ в толпе людей на сцене под фанеру рэпчик скучный\nБоже что за жесть я надеюсь что сегодня будет..."
            ))
    result.append(
            telebot.types.InlineQueryResultAudio(
            id=3, title="Дождик за окном", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="⭐️", callback_data=f"rate 3")),
            audio_url="https://mp3uks.ru/mp3/files/dora-dozhdik-za-oknom-mp3.mp3",
            caption=f"⭐️: {database['music'][3]} \nДождик за окном\nПочему? Почему? Почему? Почему?\nТы не хочешь быть со мной\nПочему? Почему? Почему? Почему?..."
            ))
    result.append(
            telebot.types.InlineQueryResultAudio(
            id=4, title="Осень пьяная", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="⭐️", callback_data=f"rate 4")),
            audio_url="https://mp3uks.ru/mp3/files/dora-osen-pyanaya-mp3.mp3",
            caption=f"⭐️: {database['music'][4]} \nХолодные ветра пылают за окном\nЖестокая игра, ведь выиграть в ней, мне не дано\nПальцами по стеклу, нетрезвые слова\nИ глупый телефон напишет за меня..."
            ))

    return result