###
import telebot

token = '8119251314:AAHp7y96qiM8FeJ2gEDr8D9rE1FhmX4xPNk'

bot = telebot.TeleBot(token)
name = "Миша"
@bot.message_handler(content_types=['text'])
def echo(message):
    if name in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop = True)
