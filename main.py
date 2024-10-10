from gettext import textdomain
from xml.sax import parse

import telebot
import webbrowser
import requests
from telebot.types import InputTextMessageContent

bot = telebot.TeleBot("8126003819:AAEsVAottHrxV-j6Jvj1iaLVspPtCPz-42I")


def avalaible(site_name):
    site = f'https://www.{site_name}'
    try:
        response = requests.get(site)
        return (f'Cайт {site} можно открыть в России!')
    except:
        return (f'Сайт {site} невозможно открыть в России ;(')


@bot.message_handler(commands=["check"])
def check(message):
    InputTextMessageContent(message_text='')
    symbol_remove = "/check "
    site_name = message.text.replace(symbol_remove,'')
    bot.send_message(message.chat.id, avalaible(site_name))


@bot.message_handler(commands=["website"])
def site(message):
    bot.send_message(message.chat.id,"https://isitblockedinrussia.com")


@bot.message_handler(commands=["start", "restart"])
def hello(message):
    bot.send_message(message.chat.id,
                     f"<b>Привет, {message.from_user.first_name}!</b>. \n\nДанный бот позволяет узнать доступность сайтов в России\n\nПример запроса:\n/check google.com",
                     parse_mode="html")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,
                     "Данный бот позволяет узнать, работает ли какой-либо сайт на территории РФ \n<b>/check</b> - проверить работоспособность сайта \n<b>/website</b> - перейти на сайт с аналогичным функционалом",
                     parse_mode="html")


bot.polling(non_stop=True)
