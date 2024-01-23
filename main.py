from dotenv import load_dotenv
import telebot
import os

import constants

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

print("Bot started...")

me  = bot.get_me()

markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
markup.add(*[telebot.types.InlineKeyboardButton(option) for option in constants.OPTIONS])


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    print(user_chat_id, first_name, last_name)

    welcome_message = f"""
    Hello {first_name} {last_name}
    """

    bot.send_message(user_chat_id, welcome_message)
    bot.send_message(user_chat_id, "Choose Options: ", reply_markup=markup)


bot.infinity_polling()