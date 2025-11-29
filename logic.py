from bot_instance import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Словарь для хранения выбранной команды пользователя
user_teams = {}
startgame = 0

# Обработчик команды /start

# Обработчик /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=2)
    
    # кнопки
    btn1 = InlineKeyboardButton('🕹️ Играть', callback_data='playbutton')
    btn2 = InlineKeyboardButton('📎 Открыть канал', url='https://t.me/kbf_1')
    
    # клавиатура
    markup.add(btn1, btn2)
    
    # соо с клавиатурой
    bot.send_message(
        message.chat.id,
        "🏆 Добро пожаловать в игрового телеграм-бота по любительскому детскому футбольному соревнованию «КБФ»",
        reply_markup=markup
    )

# обработчик нажатий 
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global startgame  # Добавляем global для изменения глобальной переменной
    
    if call.data == 'playbutton':
        bot.answer_callback_query(call.id, "🟡 Вы начали играть!")
        show_teams(call)
    
    elif call.data == 'squad_btn':
        bot.answer_callback_query(call.id, "👨 Просмотр состава")
        squadbuttons(call)

    elif call.data == 'ofice_btn':
        oficebuttons(call)

    elif call.data == 'bayan':
        bot.answer_callback_query(call.id, "⚪ Вы выбрали Баян")
        user_teams[call.message.chat.id] = 'Баян'
        show_team_info(call, 'bayan')

    elif call.data == 'dragons':
        bot.answer_callback_query(call.id, "⚫ Вы выбрали Драгонс")
        user_teams[call.message.chat.id] = 'Драгонс'
        show_team_info(call, 'dragons')
    
    elif call.data == 'energy':
        bot.answer_callback_query(call.id, "🟢 Вы выбрали Энергию")
        user_teams[call.message.chat.id] = 'Энергия'
        show_team_info(call, 'energy')

    elif call.data == 'chekushka':
        bot.answer_callback_query(call.id, "🔘 Вы выбрали Chekushka")
        user_teams[call.message.chat.id] = 'Chekushka'
        show_team_info(call, 'chekushka')

    elif call.data == 'kairat':
        bot.answer_callback_query(call.id, "🟡 Вы выбрали Kairat")
        user_teams[call.message.chat.id] = 'Kairat'
        show_team_info(call, 'kairat')

    elif call.data == 'bratishki':
        bot.answer_callback_query(call.id, "🔴 Вы выбрали Братишки")
        user_teams[call.message.chat.id] = 'Братишки'
        show_team_info(call, 'bratishki')

    elif call.data == 'mell':
        bot.answer_callback_query(call.id, "⚪ Вы выбрали Mell Team")
        user_teams[call.message.chat.id] = 'Mell Team'
        show_team_info(call, 'mell')

    elif call.data == 'shbg':
        bot.answer_callback_query(call.id, "🔵 Вы выбрали Шторм&Баграт")
        user_teams[call.message.chat.id] = 'Шторм&Баграт'
        show_team_info(call, 'shbg')

    elif call.data == 'aci':
        bot.answer_callback_query(call.id, "⚫ Ацидолакт")
        user_teams[call.message.chat.id] = 'Ацидолакт'
        show_team_info(call, 'aci')

    elif call.data == 'fortez':
        bot.answer_callback_query(call.id, "🟡 Вы выбрали Fortez")
        user_teams[call.message.chat.id] = 'Fortez'
        show_team_info(call, 'fortez')

    elif call.data == 'df':
        bot.answer_callback_query(call.id, "🔘 Вы выбрали Dragon Force")
        user_teams[call.message.chat.id] = 'Dragon Force'
        show_team_info(call, 'df')

    elif call.data == 'bratishki2':
        bot.answer_callback_query(call.id, "🔴 Вы выбрали Братишки-2")
        user_teams[call.message.chat.id] = 'Братишки-2'
        show_team_info(call, 'bratishki2')

    elif call.data == 'galaxy':
        bot.answer_callback_query(call.id, "🔵 Вы выбрали Galaxy")
        user_teams[call.message.chat.id] = 'Galaxy'
        show_team_info(call, 'galaxy')

    elif call.data == 'atlanta':
        bot.answer_callback_query(call.id, "🔘 Вы выбрали Atlanta")
        user_teams[call.message.chat.id] = 'Atlanta'
        show_team_info(call, 'atlanta')

    elif call.data == 'ok':
        bot.answer_callback_query(call.id, "✅ Вы приняли должность")
        # Получаем название команды из словаря
        team_name = user_teams.get(call.message.chat.id, 'неизвестной команды')
        start_game(call, team_name)

def show_teams(call):
    markup = InlineKeyboardMarkup(row_width=2)
    
    # кнопки разных команд
    bayan_btn = InlineKeyboardButton('⚪ Баян', callback_data='bayan')
    dragons_btn = InlineKeyboardButton('⚫ Драгонс', callback_data='dragons')
    energy_btn = InlineKeyboardButton('🟢 Энергия-Сельбагу', callback_data='energy')
    chek_btn = InlineKeyboardButton('🔘 Chekushka', callback_data='chekushka')
    kairat_btn = InlineKeyboardButton('🟡 Kairat', callback_data='kairat')
    bratishki_btn = InlineKeyboardButton('🔴 Братишки', callback_data='bratishki')
    mell_btn = InlineKeyboardButton('⚪ Mell Team', callback_data='mell')
    shbg_btn = InlineKeyboardButton('🔵 Шторм&Баграт', callback_data='shbg')
    aci_btn = InlineKeyboardButton('⚫ Ацидолакт', callback_data='aci')
    fortez_btn = InlineKeyboardButton('🟡 Fortez', callback_data='fortez')
    df_btn = InlineKeyboardButton('🔘 Dragon Force', callback_data='df')
    bratishki2_btn = InlineKeyboardButton('🔴 Братишки-2', callback_data='bratishki2')
    galaxy_btn = InlineKeyboardButton('🔵 Galaxy', callback_data='galaxy')
    atlanta_btn = InlineKeyboardButton('🔘 Atlanta', callback_data='atlanta')
    
    markup.add(bayan_btn, dragons_btn, energy_btn, chek_btn, kairat_btn, bratishki_btn, mell_btn, shbg_btn, aci_btn, fortez_btn, df_btn, bratishki2_btn, galaxy_btn, atlanta_btn)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🏆 Добро пожаловать! Выберите команду:",
        reply_markup=markup
    )

def show_team_info(call, team_name):
    global startgame  # Добавляем global для изменения глобальной переменной
    
    markup = InlineKeyboardMarkup(row_width=2)
    okbtn = InlineKeyboardButton('✅ Войти на должность', callback_data='ok')
    backbtn = InlineKeyboardButton('🔙 Назад к командам', callback_data='playbutton')
    markup.add(okbtn, backbtn)
    
    # инфо о командах
    if team_name == 'bayan':
        startgame += 1
        team_text = """
⚪ Баян

📜 История клуба:
В истории команды было множество крупных достижений, как победа в первом сезоне, а также выходы в финал во втором и четвёртом сезонах

🔅 Основание: 2024
🏆 Трофеи: 1
💰 Бюджет: 3,2 тысячи Р.
❗ Ожидания руководства: 1/2 стадии плей-офф

Готовы возглавить эту команду?"""
    elif team_name == 'dragons':
        startgame += 1
        team_text = """
⚫ Драгонс

📜 История клуба:
Лучший результат команды — выход в полуфинальную стадию четвёртого сезона

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 2,5 тысяч Р.
❗ Ожидания руководства: Занять высокие места в таблице общего этапа, достойный результат в стадии плей-офф

Готовы возглавить эту команду?"""

    elif team_name == 'energy':
        startgame += 1
        team_text = """
🟢 Энергия

📜 История клуба:
Команда в первом для себя сезоне в соревновании оформила победу, обыграв соперника в финале 5:4

🔅 Основание: 2025
🏆 Трофеи: 1
💰 Бюджет: 4,7 тысяч Р.
❗ Ожидания руководства: Выход в финальную стадию плей-офф

Готовы возглавить эту команду?"""

    elif team_name == 'chekushka':
        startgame += 1
        team_text = """
🔘 Chekushka

📜 История клуба:
В первом сезоне клуб вышел в финальную стадию, где проиграл соперникам 5:4

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 4,4 тысяч Р.
❗ Ожидания руководства: Выход в финальную стадию плей-офф

Готовы возглавить эту команду?"""

    elif team_name == 'kairat':
        startgame += 1
        team_text = """
🟡 Kairat

📜 История клуба:
-

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 3,9 тысяч Р.
❗ Ожидания руководства: Выход в 1/2 стадии плей-офф

Готовы возглавить эту команду?"""

    elif team_name == 'bratishki':
        startgame += 1
        team_text = """
🔴 Братишки

📜 История клуба:
Команда показала хороший результат в прошлом сезоне, дойдя до полуфинала

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 3,8 тысяч Р.
❗ Ожидания руководства: Выход в финальную стадию плей-офф

Готовы возглавить эту команду?"""

    elif team_name == 'mell':
        startgame += 1
        team_text = """
⚪ Mell Team

📜 История клуба:
Новичок лиги, команда с амбициозными планами и молодыми перспективными игроками

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 3,1 тысяч Р.
❗ Ожидания руководства: Достойно выступить в сезоне

Готовы возглавить эту команду?"""

    elif team_name == 'shbg':
        startgame += 1
        team_text = """
🔵 Шторм&Баграт

📜 История клуба:
Объединенная команда с богатым опытом выступлений в различных турнирах

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 3,3 тысяч Р.
❗ Ожидания руководства: Выйти в 1/2 стадию плей-офф

Готовы возглавить эту команду?"""

    elif team_name == 'aci':
        startgame += 1
        team_text = """
⚫ Ацидолакт

📜 История клуба:
Команда с уникальным стилем игры и хорошим составом

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 3,1 тысяч Р.
❗ Ожидания руководства: Продемонстрировать хороший результат за сезон

Готовы возглавить эту команду?"""

    elif team_name == 'fortez':
        startgame += 1
        team_text = """
🟡 Fortez

📜 История клуба:
Сильная команда с хорошими результатами в прошлых сезонах

🔅 Основание: 2024
🏆 Трофеи: 0
💰 Бюджет: 4,0 тысяч Р.
❗ Ожидания руководства: Борьба за чемпионство

Готовы возглавить эту команду?"""

    elif team_name == 'df':
        startgame += 1
        team_text = """
🔘 Dragon Force

📜 История клуба:
Молодая перспективная команда с большим потенциалом

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 2,8 тысяч Р.
❗ Ожидания руководства: Занять место в верхней половине таблицы

Готовы возглавить эту команду?"""

    elif team_name == 'bratishki2':
        startgame += 1
        team_text = """
🔴 Братишки-2

📜 История клуба:
Фарм-клуб основной команды, ориентированный на развитие талантов

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 1,8 тысяч Р.
❗ Ожидания руководства: Подготовка резерва для основной команды

Готовы возглавить эту команду?"""

    elif team_name == 'galaxy':
        startgame += 1
        team_text = """
🔵 Galaxy

📜 История клуба:
Занять высокие места в таблице общего этапа, достойный результат в стадии плей-офф

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 2,9 тысяч Р.
❗ Ожидания руководства: Занять 

Готовы возглавить эту команду?"""

    elif team_name == 'atlanta':
        startgame += 1
        team_text = """
🔘 Atlanta

📜 История клуба:
Занять высокие места в таблице общего этапа, достойный результат в стадии плей-офф

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 3,6 тысяч Р.
❗ Ожидания руководства: Выход в 1/4 стадии плей-офф

Готовы возглавить эту команду?"""

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=team_text,
        reply_markup=markup
    )

# Клавиатура - игра
markupgame = InlineKeyboardMarkup(row_width=2)
nextgame = InlineKeyboardButton('⚽ Сыграть матч', callback_data='game_btn')
squadbtn = InlineKeyboardButton('👨 Состав', callback_data='squad_btn')
ofice = InlineKeyboardButton('✉️ Офис', callback_data='ofice_btn')
calendar = InlineKeyboardButton('📆 Календарь', callback_data='calendar_btn')
markupgame.add(nextgame, squadbtn, ofice, calendar)

# Назад
nazad = InlineKeyboardButton('🔙 Назад', callback_data='menugame')

# Кнопки состава
squadsbtn = InlineKeyboardMarkup(row_width=2)
startsquad = InlineKeyboardButton('✍️ Стартовый состав', callback_data='startsquad')
tactic = InlineKeyboardButton('📃 Тактика', callback_data='tactic')
squadsbtn.add(startsquad, tactic, nazad)

# Кнопки офиса
oficebtns = InlineKeyboardMarkup(row_width=2)
pochta = InlineKeyboardButton('📫 Почтовый ящик', callback_data='startsquad')
oficebtns.add(pochta, nazad)

# if else кнопки игры
def squadbuttons(call):
    if call.data == 'squad_btn':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = '❗ В этой вкладке вы можете редактировать стартовый состав и изменять тактику на игру',
            reply_markup=squadsbtn)

# if else офиса
def oficebuttons(call):
    if call.data == 'ofice_btn':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = '❗ В этой вкладке вы можете смотреть почтовый ящик',
            reply_markup=oficebtns)
        
# if else календаря
def calendarbuttons(call):
    if call.data == 'calendar_btn':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text = 'в этой вкладке будет календарь игр',
            reply_markup=nazad)

def start_game(call, team_name):
    if startgame == 1:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"👋 Добро пожаловать на пост главного тренера команды «{team_name}»!",
            reply_markup=markupgame
)
