import requests 
import telebot
from telebot import types
import os
from rozetka import *



bot = telebot.TeleBot(os.getenv('telegram_id'))
@bot.message_handler(commands=['help'])
def buttons(message):
    if message.text == '/help':
        markup = types.ReplyKeyboardMarkup()
        turn_on_tv = types.KeyboardButton('Turn on the tv')
        turn_off_tv = types.KeyboardButton('Turn off the tv')
        turn_on_printer = types.KeyboardButton('Turn on the printer')
        turn_off_printer = types.KeyboardButton('Turn off the printer')
        markup.row(turn_on_tv, turn_off_tv)
        markup.row(turn_on_printer, turn_off_printer)
        bot.send_message(message.chat.id, 'Select what do you need.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_taker(message):
    if message.text == 'Turn on the printer':
        a.set_status(switch=a.set_status(a.dps['printer'], True))
    if message.text == 'Turn off the printer':
            a.set_status(switch=a.set_status(a.dps['printer'], False))
             
bot.polling(none_stop=True, interval=0)