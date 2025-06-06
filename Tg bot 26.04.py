import telebot
import threading
from telebot import storage

# Инициализация бота
b = telebot.TeleBot("7603926821:AAGX11STbfXOC8OAlDGi6wFQ5Ph4EBJ7_fw")
s = storage.StateMemoryStorage()

# Словарь состояний
u = {}


# Обработчик /start
@b.message_handler(commands=['start'])
def a(m):
    b.reply_to(m, "Я бот для напоминаний. Используй  /remind чтобы установить напоминание.")


# Обработчик /remind
@b.message_handler(commands=['remind'])
def c(m):
    i = m.chat.id
    u[i] = 't'
    b.send_message(i, "Через сколько минут напомнить?")


# Обработчик текста
@b.message_handler(func=lambda m: True)
def d(m):
    i = m.chat.id

    if i in u and u[i] == 't':
        try:
            n = float(m.text)
            if n <= 0:
                b.send_message(i, "введите положительное число.")
                return

            x = n * 60
            r = f"Напоминание сработало! "

            # Таймер
            t = threading.Timer(x, e, args=[i, r])
            t.start()

            b.send_message(i, f"Хорошо, напомню через {n} минут.")
            del u[i]

        except ValueError:
            b.send_message(i, "введите число например: 5 или 2.5.")


# Отправка напоминания
def e(i, r):
    b.send_message(i, r)


# Запуск
if __name__ == '__main__':
    print("Бот запущен...")
    b.infinity_polling()

