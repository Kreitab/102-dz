import telebot
import threading
from telebot import storage
bot = telebot.TeleBot("7369053556:AAHEMinT33s5LBkr7QXGMRcNXRpK7u2BVF8")
state_storage = storage.StateMemoryStorage()
vremy = {}
@bot.message_handler(commands=['start'])
def priv(message):
    bot.reply_to(message, "Привет тут ты сможешь установить напоминание с помощью /remind")
@bot.message_handler(commands=['remind'])
def nap(message):
    x = message.chat.id
    vremy[x] = 'waiting_for_time'
    bot.send_message(x, "Через сколько минут напоминание сработает?")
@bot.message_handler(func=lambda message: True)
def otvet(message):
    x = message.chat.id

    if x in vremy and vremy[x] == 'waiting_for_time':
        try:
            min = float(message.text)
            if min <= 0:
                bot.send_message(x, "Должно быть положительное число")
                return
            sec = min * 60
            text = f"Напоминание!"

            timer = threading.Timer(sec, h, args=[x, text])
            timer.start()
            bot.send_message(x, f"Напишу через {min} ")
            del vremy[x]
        except ValueError:
            bot.send_message(x, "Тут должно быть написано число")
def h(x, otvet):
    bot.send_message(x, otvet)
if __name__ == '__main__':
    bot.infinity_polling()

