import telebot

bot = telebot.TeleBot(token='8157684832:AAFQx0uIE4yXvqa7RGQ1GY6-NilBa6FmeAs')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

bot.infinity_polling()