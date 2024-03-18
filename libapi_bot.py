import telebot
import pprint
import time

token = '6623809896:AAEzuCEjCUQfcLlUjnIe_XGvDV-03NkdHoQ'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, text='Как твои дела? Чем я могу помочь?')


@bot.message_handler(content_types=['timer'])
def say(message):
    for i in range(1000):
        time.sleep(0.5)
        bot.send_message(message.chat.id, i + 1)


@bot.message_handler(content_types=['say'])
def say(message):
    text = ''.join(message.text.split(' ')[1:])
    bot.reply_to(message, text=f'***{text.upper()}!***')


@bot.message_handler(content_types='sticker')
def send_sticker(message):
    print(message)
    file_ID = 'AAMCAgADGQEAAzll-GMCojBhGpHTgw1E7ttlp-pO_wAC-zwAArrV6UtkjR1jMueNXQEAB20AAzQE'
    bot.send_sticker(message.chat.id, id, file_ID)


@bot.message_handler(content_say='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, text='Текст содержит слово плохой')
        return
    text = message.text[:: -1]
    bot.reply_to(message, text)


bot.polling()
