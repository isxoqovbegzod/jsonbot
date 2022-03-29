import requests
import telebot
import json
TOKEN = '5295753057:AAGVOAPzjyxlOcqFrj45CpWmY4aMfGndsbs'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, "Assalom\nSo'z kiriting")


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    id_ = message.from_user.id
    message_id = message.text
    URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id_}&text={message_id}"
    r = requests.get(URL).json()
    a = json.dumps(r, indent=1)

    bot.send_message(id_, text=f'<code>{a}</code> ', parse_mode='html')


bot.infinity_polling()

