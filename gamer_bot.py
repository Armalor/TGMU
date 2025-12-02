from telebot import TeleBot
from telebot.types import ChatMemberOwner, ChatMemberAdministrator
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


class BotConfig:
    def __init__(self):
        self.token = '8464798499:AAHqmqmTCbYE74f5caboD2QCzypH8k9WMck'
        self.url = 't.me/PlayerTGMUBot'


config = BotConfig()

bot = TeleBot(config.token, parse_mode='HTML')


@bot.message_handler(commands=['auth'])
def auth(message):
    bot.send_message(
        message.chat.id,
        f"Привет! chat_id = {message.chat.id}; user_id = {message.from_user.id}"
    )


@bot.message_handler(commands=['start'])
def start(message):
    inline_kb = InlineKeyboardMarkup(row_width=2)
    poker_btn = InlineKeyboardButton('Покер!', callback_data='poker')
    roulette_btn = InlineKeyboardButton('Рулетка!', callback_data='roulette')
    slot_btn = InlineKeyboardButton('Однорукий бандит!', callback_data='slot')
    inline_kb.add(poker_btn, roulette_btn, slot_btn)

    exit_btn = InlineKeyboardButton('Не, я на выход', callback_data='exit')
    inline_kb.add(exit_btn)

    bot.send_message(
        message.chat.id,
        f"Приветствуем вас в нашем казино! Где желаете сыграть?",
        reply_markup=inline_kb
    )


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('poker'))
def pocker_callback(callback_query: CallbackQuery):
    buttons = [
        KeyboardButton('кнопка 1'),
        KeyboardButton('кнопка 2'),
        KeyboardButton('кнопка 3'),
    ]

    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*buttons)
    bot.send_message(callback_query.message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "кнопка 1":
        markup=ReplyKeyboardMarkup(one_time_keyboard=True)
        item1=KeyboardButton("Кнопка 11")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Кнопка 1 →', reply_markup=markup)
    elif message.text == "кнопка 2":
        bot.send_message(message.chat.id, 'Спасибо за визит!')


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('roulette'))
def roulette_callback(callback_query):
    print(callback_query)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('slot'))
def slot_callback(callback_query):
    print(callback_query)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('exit'))
def exit_callback(callback_query):
    bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
    )


if __name__ == '__main__':
    bot.polling()
