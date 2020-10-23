import telebot
from telebot import TeleBot
import requests

chat_ids_file = 'chat_ids.txt'
ADMIN_CHAT_ID = 306433726
block_list = 'block_list.txt'

group_id = -1001177812238

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types

running_spams_per_chat_id = []

type_messages = int()

class TelegramBot:

    def __init__(self, token, limit_threads):
        self.token = token
        self.bot = TeleBot(token)
        self.bot.polling(none_stop=True, interval=0)
        self.limit_threads = limit_threads

    def response_post(self, token, data):
        response = requests.post(
            'https://api.telegram.org/bot' + token + '/sendMessage (https://api.telegram.org/bot' + token + '/sendMessage)',
            data=data)
        res = str(response.json)
        print(res)
        if res == '<bound method Response.json of <Response [403]>>':
            with open(chat_ids_file, "r") as f:
                lines = f.readlines()
            with open(chat_ids_file, "w") as f:
                for line in lines:
                    if line.strip("\n") != data['chat_id']:
                        f.write(line)
        else:
            return True

    def send_message(self, chat_id, message):
        token = self.token
        data = {
            'chat_id': chat_id,
            'text': message
        }
        self.response_post(token, data)

    def send_message_users(self, message):
        with open(chat_ids_file, "r") as ids_file:
            ids_list = [line.split('\n')[0] for line in ids_file]

        [self.send_message(chat_id, message) for chat_id in ids_list]
        self.send_message(ADMIN_CHAT_ID, f'Сообщение всем пользователям бота успешно дошло!')

    def generate_buttons(self):
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        boom = types.KeyboardButton(text='🔥💣БОМБЕР')
        titan = types.KeyboardButton(text='👅💦Титан-ГЕЛЬ')
        stop = types.KeyboardButton(text='⛔️STOP')
        info = types.KeyboardButton(text='ℹ️Информация')
        stats = types.KeyboardButton(text='📈Статистика')
        donat = types.KeyboardButton(text='💰Поддержать')
        piar = types.KeyboardButton(text='💸 Реклама')
        spons = types.KeyboardButton(text='🤝Наш партнер')

        buttons_to_add = [boom, titan, stop, info, stats, donat, piar, spons]

        keyboard.add(*buttons_to_add)