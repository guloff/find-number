"""Version 1.1"""
import telebot
from telebot import types
import random
import time
import json

bot = telebot.TeleBot('1233473633:AAFLvRF0qb-xy5fFMz8SXuDeW-BYWK1_Lbc')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    button1 = types.KeyboardButton('Играть')
    button2 = types.KeyboardButton('Позже')
    markup.add(button1, button2)
    msg_text = f"Привет, <strong>{message.from_user.first_name}</strong>! Поиграем? Сможете угадать число, которое я загадал? Нажмите 'Играть', чтобы начать игру."
    bot.send_message(message.chat.id, msg_text, parse_mode = 'html', reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    msg_text = message.text.strip().lower()
    if msg_text == 'позже':
        reply_msg_text = "Хорошо! Поиграем позже :) Как будете готовы, нажмите кнопку 'Играть'."
        bot.send_message(message.chat.id, reply_msg_text)
    elif msg_text == 'играть':
        start_of_range = random.randrange(1,100)
        stop_of_range = random.randrange(900,1000)
        global number
        number = random.randrange(start_of_range, stop_of_range)
        global counter
        counter = 0
        global start_time
        start_time = time.time()

        reply_msg_text = f"Круто! Я загадал число в диапазоне между {start_of_range} и {stop_of_range}. Посмотрим, за сколько попыток вы сможете угадать. Пришлите мне любое число в заданном диапазоне."
        bot.send_message(message.chat.id, reply_msg_text)
    try:
        if msg_text.isnumeric():
            user_guess_number = int(msg_text)
            # Старт кода игры
            # n = True
            if user_guess_number < number:
                counter += 1
                notification_text = f"<strong>Попытка №{counter}</strong>. Нет, маловато. Загаданное число больше {user_guess_number}."
            elif user_guess_number > number:
                counter += 1
                notification_text = f"<strong>Попытка №{counter}</strong>. Нет, это больше загаданного. Попробуйте число меньше {user_guess_number}."
            elif user_guess_number == number:
                counter += 1
                # Потрачено времени на игру
                finish_time = time.time()
                gametime = str(round(finish_time - start_time))
                nums_0_14 = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                nums_2_4 = [2, 3, 4]
                # Склонение слова "секунда"
                if int(gametime) in nums_0_14:
                    sec_word = 'секунд'
                elif int(gametime[-1]) == 1:
                    sec_word = 'секунду'
                elif int(gametime[-1]) in nums_2_4:
                    sec_word = 'секунды'
                else:
                    sec_word = 'секунд'

                # Склонение слова "попытка"
                counter = str(counter)
                if int(counter) in nums_0_14:
                    counter_word = 'попыток'
                elif int(counter[-1]) == 1:
                    counter_word = 'попытку'
                elif int(counter[-1]) in nums_2_4:
                    counter_word = 'попытки'
                else:
                    counter_word = 'попыток'

                # Результат игры
                results = {
                    'user_id': message.from_user.id,
                    'user_first_name': message.from_user.first_name,
                    'user_last_name': message.from_user.last_name,
                    'tries': counter,
                    'gametime': gametime,
                    'timestamp': start_time,
                }
                # Запись результата в файле
                with open('leaderboard.json', 'a') as f:
                    json.dump(results, f)

                notification_text = f"Круто! Поздравляю <strong>{message.from_user.first_name}</strong>, вы нашли загаданное мною число за <strong>{counter} {counter_word}</strong>, потратив на игру <strong>{gametime} {sec_word}</strong>!"
            bot.send_message(message.chat.id, notification_text, parse_mode = 'html')
            # Финал кода игры
    except NameError:
        notification_text = "Кажется, мы еще не начали играть. Пожалуйста, нажмите 'Играть'"
        bot.send_message(message.chat.id, notification_text)

    if msg_text != 'позже' and msg_text != 'играть' and not msg_text.isnumeric():
        reply_text = "Я не понимаю других команд, кроме 'Позже', 'Играть' и чисел. Введите 'Играть', если хотите начать игру или 'Позже', если хотите поиграть позже."
        bot.send_message(message.chat.id, reply_text)

bot.polling(none_stop = True, interval = 0)
