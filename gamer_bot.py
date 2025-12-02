from telebot import TeleBot
from telebot.types import ChatMemberOwner, ChatMemberAdministrator
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


class BotConfig:
    def __init__(self):
        self.token = '8464798499:AAHqmqmTCbYE74f5caboD2QCzypH8k9WMck'
        self.url = 't.me/PlayerTGMUBot'
        self.parse_mode = 'HTML'


config = BotConfig()

bot = TeleBot(config.token, parse_mode=config.parse_mode)


@bot.message_handler(commands=['auth'])
def auth(message):

    bot.send_message(
        message.chat.id,
        f"Привет! chat_id = {message.chat.id}; user_id = {message.from_user.id}"
    )


@bot.message_handler(commands=['start'])
def start(message):

    bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.id,
    )

    inline_kb = InlineKeyboardMarkup(row_width=2)

    poker_btn = InlineKeyboardButton('Покер', callback_data='poker')
    roulette_btn = InlineKeyboardButton('Рулетка', callback_data='roulette')
    slot_btn = InlineKeyboardButton('Однорукий бандит', callback_data='slot')

    inline_kb.add(poker_btn, roulette_btn, slot_btn)

    exit_btn = InlineKeyboardButton('Не, я на выход', callback_data='exit')
    inline_kb.add(exit_btn)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Приветствует вас в казино! Во что хотите сыграть?",
        reply_markup=inline_kb
    )


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('exit'))
def exit_callback(callback_query):
    bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
    )


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('slot'))
def slot_callback(callback_query):
    b1 = KeyboardButton('автомат 1')
    b2 = KeyboardButton('автомат 2')
    b3 = KeyboardButton('автомат 3')

    rkb = ReplyKeyboardMarkup(one_time_keyboard=True)

    rkb.add(b1, b2, b3)

    bot.send_message(callback_query.message.chat.id, 'Выберите автомат, который вам нужен!', reply_markup=rkb)


@bot.message_handler(content_types=['text'])
def replay_handler(message):
    if message.text == 'автомат 1':
        bot.send_message(message.chat.id, 'Вы играете на автомате №1')
    elif message.text == 'автомат 2':
        rkb = ReplyKeyboardMarkup(one_time_keyboard=True)
        b2 = KeyboardButton('Крутить барабан автомата 2')
        rkb.add(b2)
        bot.send_message(message.chat.id, 'Пошла игра:', reply_markup=rkb)


if __name__ == '__main__':
    bot.polling()