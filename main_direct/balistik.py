from telebot import types
import telebot
from dotenv import dotenv_values
from config.env_config import *
import os
from telebot.types import ReplyKeyboardRemove
import math
import matplotlib.pyplot as plt
from Language.English import translations as en
from Language.Ukrainian import translations as uk
from Language.Russian import translations as ru
from bullet.types_bull import Bullet

config_1 = dotenv_values("../.env")
user_language = {}
bot=telebot.TeleBot(TOKEN)
bot.timeout = 30


def get_text(user_id, key):
    language = user_language.get(user_id, "en")
    if language == "ru":
        return ru.get(key, "⚠️ Перевод не найден")
    elif language == "uk":
        return uk.get(key, "⚠️ Переклад не знайден")
    else:
        return en.get(key,"⚠️ Translation not found")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"This support Balistik bot")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne=types.KeyboardButton("Choose language")
    butTwo=types.KeyboardButton("/close")
    markup.add(butOne,butTwo)
    bot.send_message(message.chat.id,"Lets start,Почнемо,Давай начнем",reply_markup=markup)

@bot.message_handler(commands=["close"])
def close(message):
    bot.send_message(message.chat.id,"<em><b>Thank you.We stay with you</b></em>",parse_mode="html")
    bot.send_message(
        message.chat.id,
        "Goodbye!",
        reply_markup=ReplyKeyboardRemove()
    )
    chat_id = message.chat.id
    last_message_id = message.message_id
    for msg_id in range(last_message_id, last_message_id - 100, -1):
        try:
            bot.delete_message(chat_id, msg_id)
        except:
            pass

@bot.message_handler(func=lambda message: message.text == "Choose language")
def choose_language(message):
    if message.text == "Choose language":
        bot.send_message(message.chat.id, "Choose language    Обери мову    Выбери язык")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("English")
        butTwo = types.KeyboardButton("Русский")
        butThree = types.KeyboardButton("Українська")
        butFour = types.KeyboardButton("/close")
        markup.add(butOne, butTwo, butThree,butFour)
        bot.send_message(message.chat.id, "Lets start,Почнемо,Давай начнем", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["English", "Русский", "Українська"])
def set_language(message):
    if message.text == "English":
        user_language[message.chat.id] = "en"
        bot.send_message(message.chat.id,get_text(message.chat.id,"choose"))
    elif message.text == "Русский":
        user_language[message.chat.id] = "ru"
        bot.send_message(message.chat.id, get_text(message.chat.id, "choose"))
    else:
        user_language[message.chat.id] = "uk"
        bot.send_message(message.chat.id, get_text(message.chat.id, "choose"))

    start_calculate(message)


def start_calculate(message):
    user_id = message.chat.id
    text = get_text(user_id, "enter_num_1")
    bot.send_message(user_id, text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne = types.KeyboardButton("1")
    butTwo = types.KeyboardButton("2")
    butThree = types.KeyboardButton("3")
    butFour = types.KeyboardButton("4")
    butFive = types.KeyboardButton("/close")
    markup.add(butOne, butTwo, butThree, butFour, butFive)
    bot.send_message(message.chat.id, "Lets start,Почнемо,Давай начнем", reply_markup=markup)
    bot.send_message(message.chat.id, """1. 9mm: mass=0.008 kg, BC=0.15, speed=380 m/s
2. 308_win: mass=0.00945 kg, BC=0.45, speed=820 m/s
3. 556_nato: mass=0.004 kg, BC=0.3, speed=950 m/s
4. 762x39: mass=0.008 kg, BC=0.275, speed=715 m/s""", reply_markup=markup)
@bot.message_handler(content_types=['text','photo'])
def calculate(message):
    user_id = message.chat.id
    text = get_text(user_id, "Error")
    if message.text == "1":
        bot.send_message(message.chat.id, "9mm: mass=0.008 kg, BC=0.15, speed=380 m/s")
        return 1
    elif message.text == "2":
        bot.send_message(message.chat.id, "308_win: mass=0.00945 kg, BC=0.45, speed=820 m/s")
        return 2
    elif message.text == "3":
        bot.send_message(message.chat.id, "556_nato: mass=0.004 kg, BC=0.3, speed=950 m/s")
        return 3
    elif message.text == "4":
        bot.send_message(message.chat.id, "556_nato: mass=0.004 kg, BC=0.3, speed=950 m/s")
        return 4
    else:
        bot.send_message(message.chat.id, "Error")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butFive = types.KeyboardButton("/close")
        markup.add( butFive)
        bot.send_message(message.chat.id, text, reply_markup=markup)



if __name__=="__main__":
    bot.infinity_polling()