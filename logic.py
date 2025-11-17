from bot_instance import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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
    if call.data == 'playbutton':
        bot.answer_callback_query(call.id, "🟡 Вы начали играть!")
        show_teams(call)
    
    elif call.data == 'bayan':
        bot.answer_callback_query(call.id, "⚪ Вы выбрали Баян")
        show_team_info(call, 'bayan')

    elif call.data == 'dragons':
        bot.answer_callback_query(call.id, "⚫ Вы выбрали Драгонс")
        show_team_info(call, 'dragons')
    
    elif call.data == 'energy':
        bot.answer_callback_query(call.id, "🟢 Вы выбрали Энергию")
        show_team_info(call, 'energy')

    elif call.data == 'ok':
        bot.answer_callback_query(call.id, "✅ Вы приняли должность")
        start_game(call)

def show_teams(call):
    markup = InlineKeyboardMarkup(row_width=2)
    
    # кнопки разных команд
    bayan_btn = InlineKeyboardButton('⚪ Баян', callback_data='bayan')
    dragons_btn = InlineKeyboardButton('⚫ Драгонс', callback_data='dragons')
    energy_btn = InlineKeyboardButton('🟢 Энергия-Сельбагу', callback_data='energy')
    
    markup.add(bayan_btn, dragons_btn, energy_btn)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🏆 Добро пожаловать! Выберите команду:",
        reply_markup=markup
    )

def show_team_info(call, team_name):
    markup = InlineKeyboardMarkup(row_width=2)
    okbtn = InlineKeyboardButton('✅ Войти на должность', callback_data='ok')
    backbtn = InlineKeyboardButton('🔙 Назад к командам', callback_data='playbutton')
    markup.add(okbtn, backbtn)
    
    # инфо о командах
    if team_name == 'bayan':
        team_text = """
⚪ Баян

📜 История клуба:
В истории команды было множество крупных достижений, как победа в первом сезоне, а также выходы в финал во втором и четвёртом сезонах

🔅 Основание: 2024
🏆 Трофеи: 1
💰 Бюджет: 3,2 тысячи Р.
❗ Ожидания руководства: 1/2 стадии плей-офф

Готовы возглавить эту команду?"""
    if team_name == 'dragons':
        team_text = """
⚫ Драгонс

📜 История клуба:
Лучший результат команды — выход в полуфинальную стадию четвёртого сезона

🔅 Основание: 2025
🏆 Трофеи: 0
💰 Бюджет: 2,5 тысяч Р.
❗ Ожидания руководства: Занять высокие места в таблице общего этапа, достойный результат в стадии плей-офф

Готовы возглавить эту команду?"""

    if team_name == 'energy':
        team_text = """
🟢 Энергия

📜 История клуба:
Команда в первом для себя сезоне в соревновании оформила победу, обыграв соперника в финале 5:4

🔅 Основание: 2025
🏆 Трофеи: 1
💰 Бюджет: 4,7 тысяч Р.
❗ Ожидания руководства: Выход в финальную стадию плей-офф

Готовы возглавить эту команду?"""

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=team_text,
        reply_markup=markup
    )

def start_game(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="🎮 Игра началась! Вы теперь менеджер команды Баян!"
    )


