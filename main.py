import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import os
from services import send_for_number
from titan_gelik import send_for_titan

TOKEN = 'token'

THREADS_LIMIT = 2

chat_ids_file = 'chat_ids.txt'

block_list = 'block_list.txt'

ADMIN_CHAT_ID = 306433726

group_id = -1001177812238

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

type_messages = int()


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


def send_message_users(message):
    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }

        response = requests.post(
            'https://api.telegram.org/bot' + TOKEN + '/sendMessage (https://api.telegram.org/bot' + TOKEN + '/sendMessage)',
            data=data)
        res = str(response.json)
        print(res)
        if res == '<bound method Response.json of <Response [403]>>':
            with open(chat_ids_file, "r") as f:
                lines = f.readlines()
            with open(chat_ids_file, "w") as f:
                for line in lines:
                    if line.strip("\n") != chat_id:
                        f.write(line)
        else:
            pass

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, f'Сообщение всем ({users_amount[0]}) пользователям бота успешно дошло!')


def posts(message):
    f = open("friend.txt", mode="w", encoding="utf-8")
    f.write(message.text)
    f.close()
    bot.send_message(message.chat.id, "Описание партнера успешно обновлено")


def subchan(message):
    f = open('url.txt', mode='w', encoding='utf-8')
    f.write(message.text)
    f.close()
    bot.send_message(message.chat.id, 'Ссылка обновлена')


def postsRES():
    f = open("friend.txt", mode="w", encoding="utf-8")
    f.write("""
     Реклама - 🤝Наш партнёр
  24 часа (1 день) + 1 рассылка - 200₽
  48 часов (2 дня) + 1 рассылка - 250₽
  120 часов (5 дней) + 1 рассылка - 400₽
  Ваш текст будет во вкладке 🤝Наш партнёр""")
    f.close()


@bot.message_handler(commands=['start'])
def start(message):

    some_var = bot.get_chat_member(group_id, message.chat.id)
    user_status = some_var.status

    url = open('url.txt', 'r')

    global inl_keyboard
    inl_keyboard = types.InlineKeyboardMarkup()
    s = types.InlineKeyboardButton(text='Подписаться', url=url.read())
    inl_keyboard.add(s)
    # print(some_var)
    # print(user_status)
    if user_status == 'member' or user_status == 'administrator' or user_status == 'creator':
        bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nВыберите действие:', reply_markup=keyboard)

    if user_status == 'restricted' or user_status == 'left' or user_status == 'kicked':
        bot.send_message(message.chat.id,
                         'Вы не подписаны на наш канал.\nПодпишитесь на него чтобы получить доступ к боту.',
                         reply_markup=inl_keyboard)

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    if type_messages == 0 and force:
        msg = 'Спам запущен на неограниченое время для номера +' + phone_number
        bot.send_message(chat_id, msg)
        while True:
            if chat_id not in running_spams_per_chat_id:
                break
            send_for_number(phone_number)
        bot.send_message(chat_id, 'Спам на номер +' + phone_number + ' завершён')
        THREADS_AMOUNT[0] -= 1
        try:
            running_spams_per_chat_id.remove(chat_id)
        except Exception:
            pass

    elif type_messages == 0:
        msg = 'Спам запущен на 10000 минут на номер +' + phone_number
        bot.send_message(chat_id, msg)

        end = datetime.now() + timedelta(minutes=10000)
        while (datetime.now() < end) or (force and chat_id == ADMIN_CHAT_ID):
            if chat_id not in running_spams_per_chat_id:
                break
            send_for_number(phone_number)
        bot.send_message(chat_id, 'Спам на номер +' + phone_number + ' завершён')
        THREADS_AMOUNT[0] -= 1
        try:
            running_spams_per_chat_id.remove(chat_id)
        except Exception:
            pass

    if type_messages == 1:
        msg = 'Идет заказ титан геля на номер +' + phone_number
        bot.send_message(chat_id, msg)
        send_for_titan(phone_number)
        bot.send_message(chat_id, "Титан гели были успешно заказаны")



def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id,
                         'Вы уже начали рассылку спама. Дождитесь окончания или нажмите STOP и поробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут')
        print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):

    some_var = bot.get_chat_member(group_id, message.chat.id)
    user_status = some_var.status

    url = open('url.txt', 'r')
    inl_keyboard = types.InlineKeyboardMarkup()
    s = types.InlineKeyboardButton(text='Подписаться', url=url.read())
    inl_keyboard.add(s)

    adm = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    a = types.KeyboardButton(text='Рассылка')
    b = types.KeyboardButton(text='Предложить рекламу')
    c = types.KeyboardButton(text='Добавить партнер')
    d = types.KeyboardButton(text='Удалить партнера')
    vpn = types.KeyboardButton(text='Обновить VPN')
    sub = types.KeyboardButton(text='Изменить ссылку на канал')
    file = types.KeyboardButton(text='Dump DB')
    e = types.KeyboardButton(text='Назад')
    adm.add(a, b, c, d, vpn, sub, file, e)

    chat_id = int(message.chat.id)
    text = message.text

    some_var = bot.get_chat_member(group_id, message.chat.id)
    user_status = some_var.status

    global type_messages

    if user_status == 'member' or user_status == 'administrator' or user_status == 'creator':

        if text == "Добавить партнер" and chat_id == ADMIN_CHAT_ID:
            a = bot.send_message(message.chat.id, "Пришлите рекламу вашего партнера:")
            bot.register_next_step_handler(a, posts)

        elif text == 'Изменить ссылку на канал' and chat_id == ADMIN_CHAT_ID:
            b = bot.send_message(message.chat.id, 'Введите ссылку на канал')
            bot.register_next_step_handler(b, subchan)

        elif text == 'Удалить партнера' and chat_id == ADMIN_CHAT_ID:
            postsRES()
            bot.send_message(chat_id, 'Партнер удалён')

        elif text == 'ℹ️Информация':
            bot.send_message(chat_id,
                             'Владелец бота: @kataklizm_3000 \nПо вопросам сотрудничества обращаться в ЛС\nБот работает пока что только на Россию и Украину')

        elif text == '🔥💣БОМБЕР':
            bot.send_message(chat_id, 'Введите номер в формате:\n🇷🇺 79xxxxxxxxx\n🇺🇦 380xxxxxxxxx')
            type_messages = 0

        elif text == '👅💦Титан-ГЕЛЬ':
            bot.send_message(chat_id, 'Введите номер в формате:\n🇷🇺 79xxxxxxxxx\n🇺🇦 380xxxxxxxxx')
            type_messages = 1

        elif text == '📈Статистика':
            with open('chat_ids.txt') as f:
                size = sum(1 for _ in f)
            bot.send_message(chat_id, '📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: ' + str(
                size) + '\nСервисов для RU🇷🇺: 30\nСервисов для UK🇺🇦: 30\nБот запущен: 29.03.2020')

        elif text == '💰Поддержать':
            bot.send_message(chat_id,
                             'Ребята, кто может материально помочь на развитие бота\nВот реквизиты\nQIWI карта: ' + '<pre>---</pre>',
                             parse_mode="HTML")

        elif text == '💸 Реклама':
            bot.send_message(chat_id, """
 Реклама - рассылка:
 Цена: 150₽
 Каждый пользователь получит уведомление с вашим текстом.

 Реклама - 🤝Наш партнёр
 24 часа (1 день) + 1 рассылка - 250₽
 48 часов (2 дня) + 1 рассылка - 300₽
 120 часов (5 дней) + 1 рассылка - 500₽
 Ваш текст будет во вкладке 🤝Наш партнёр

 Купить: @kataklizm_3000  """)

        elif text == '/admin' and chat_id == ADMIN_CHAT_ID:
            bot.send_message(chat_id, 'Выберите действие.', reply_markup=adm)

        elif text == 'Назад' and chat_id == ADMIN_CHAT_ID:
            bot.send_message(chat_id, 'Выберите действие.', reply_markup=keyboard)

        elif text == 'Рассылка' and chat_id == ADMIN_CHAT_ID:
            bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

        elif text == 'Обновить VPN' and chat_id == ADMIN_CHAT_ID:
            bot.send_message(chat_id, 'Бот перезапускается...')
            os.system('python3 start.py')

        elif text == 'Dump DB' and chat_id == ADMIN_CHAT_ID:
            f = open('chat_ids.txt')
            bot.send_document(chat_id, f)

        elif text == '🤝Наш партнер':
            post = ""
            f = open("friend.txt", mode="r", encoding="utf-8")
            for line in f.readlines():
                post += line
            bot.send_message(message.chat.id, post)
            f.close()



        elif text == 'Предложить рекламу' and chat_id == ADMIN_CHAT_ID:
            bot.send_message(message.chat.id, 'Рассылка началась')
            predlog = '✅Не знаете где дать рекламу качественно и не дорого?\n🏛Тогда вы по адресу!!!\n\n👥 У нас вашу рекламу увидят все пользователи бота\n📨 @sms_spamerbot\n\n🗣 Каждый пользователь получит сообщение от бота с вашей рекламой!\n☀️ ' + str(
                users_amount[
                    0]) + ' ☀️ активных пользователей!\n\n💶 Цена рассылки: 150 ₽\n\nРеклама - 🤝Наш партнёр\n24 часа (1 день) + 1 рассылка - 250₽\n48 часов (2 дня) + 1 рассылка - 300₽\n120 часов (5 дней) + 1 рассылка - 500₽\nВаш текст будет во вкладке 🤝Наш партнёр\n\nКупить: @kataklizm_3000 '
            send_message_users(predlog)
            bot.send_message(chat_id, 'Рассылка завершена')

        elif text == '⛔️STOP':
            if chat_id not in running_spams_per_chat_id:
                bot.send_message(chat_id, 'Вы еще не начинали спам')
            else:
                running_spams_per_chat_id.remove(chat_id)

        elif 'РАЗОСЛАТЬ: ' in text and chat_id == ADMIN_CHAT_ID:
            msg = text.replace("РАЗОСЛАТЬ: ", "")
            bot.send_message(message.chat.id, 'Рассылка началась')
            send_message_users(msg)
            bot.send_message(chat_id, 'Рассылка завершена')


        elif len(text) == 11:
            phone = text
            with open(block_list) as file:
                if phone in file:
                    bot.send_message(chat_id, 'Номер в блок листе!')
                else: spam_handler(phone, chat_id, force=False)

        elif len(text) == 12:
            phone = text
            with open(block_list) as file:
                if phone in file:
                    bot.send_message(chat_id, 'Номер в блок листе!')
                else:
                    spam_handler(phone, chat_id, force=False)


        elif len(text) == 12 and chat_id == ADMIN_CHAT_ID and text[0] == '_':
            phone = text[1:]
            spam_handler(phone, chat_id, force=True)

        else:
            bot.send_message(chat_id, 'Номер введен неправильно.')

    if user_status == 'restricted' or user_status == 'left' or user_status == 'kicked':
        bot.send_message(message.chat.id,
                         'Вы не подписаны на наш канал.\nПодпишитесь на него, чтобы получить доступ к боту.',
                         reply_markup=inl_keyboard)


bot.polling(none_stop=True, interval=0)