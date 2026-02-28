import telebot
import os

TOKEN = '7891278144:AAHGf055z_4vO_2A_uP7Ff-D0O5R5h_A1_0'
bot = telebot.TeleBot(TOKEN)

print('ARIA: Sistema Python activo. Escuchando...')

@bot.message_handler(func=lambda m: True)
def respuesta(message):
    if 'ARIA??' in message.text:
        bot.reply_to(message, 'dime')
        print('ARIA: He respondido al Amo Leo.')

bot.infinity_polling()
