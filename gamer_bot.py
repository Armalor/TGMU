from telebot import TeleBot


class BotConfig:

    def __init__(self):
        self.token = '8464798499:AAHqmqmTCbYE74f5caboD2QCzypH8k9WMck'
        self.url = 't.me/PlayerTGMUBot'


config = BotConfig()

bot = TeleBot(config.token, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Привет! chat_id = {message.chat.id}; user_id = {message.from_user.id}"
    )


if __name__ == '__main__':

    print(dir())
