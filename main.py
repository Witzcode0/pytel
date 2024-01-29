from dotenv import load_dotenv
import telebot
import os
import string

import constants
from db_mysql import fatch_countries

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


@bot.message_handler(func=lambda message: message.text in constants.OPTIONS)
def handle_options(message):
    user_chat_id = message.chat.id
    selected_option = message.text

    if selected_option == 'Get Country Information':
        get_char_for_find_country_list(user_chat_id, message)
    elif selected_option == 'Generate QR':
        generate_and_send_qr(user_chat_id, message)
    elif selected_option == 'Contact Us':
        contact_us(user_chat_id)
    elif selected_option == 'Help':
        help(user_chat_id)

def get_char_for_find_country_list(user_chat_id, message):
    """
    This function for create alphabet options
    """
    alphabet_array = list(string.ascii_uppercase)
    alphabe_markup = telebot.types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
    alphabe_markup.add(*[telebot.types.KeyboardButton(ch) for ch in alphabet_array])
    bot.send_message(user_chat_id, "Choose the first letter of the country.", reply_markup=alphabe_markup)
    bot.register_next_step_handler(message, get_first_letter_of_country)

def  get_first_letter_of_country(message):
    user_chat_id = message.chat.id
    print("CH : ", message.text)
    countries_array = fatch_countries.get_specific_char_to_countries(message.text)
    countries_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    countries_markup.add(*[telebot.types.KeyboardButton(country[1]) for country in countries_array])
    bot.send_message(user_chat_id, "Choose the country.", reply_markup=countries_markup)
    bot.register_next_step_handler(message, get_specifi_country)

def get_specifi_country(message):
    user_chat_id = message.chat.id
    country = fatch_countries.get_specific_country_details(message.text)
    country_data = f"""
    Name : {country[1]}\nFlag : {country[3]}\nIndependent : {country[4]}\nOfficial_name : {country[6]}\nCapital City : {country[7]}\nContinent : {country[8]}\nMembers of : {country[9]}\nTotal Area : {country[11]}\nCurrency : {country[15].split("(")[0].strip()}\nCalling Code: {country[16]}\n Internet Tld : {country[17]}
    """
    bot.send_message(user_chat_id,country_data)
    bot.send_message(user_chat_id, "Start Again /start")

def generate_and_send_qr(user_chat_id, message):
    # Replace 'PATH_TO_PHOTO' with the path to the photo you want to send
    photo_path = 'PATH_TO_PHOTO'

    # Send the photo
    with open(photo_path, 'rb') as photo:
        bot.send_photo(user_chat_id, photo)


def contact_us(user_chat_id):
    bot.send_message(user_chat_id, """For any inquiries or assistance, please feel free to reach out to us via email: contact@wcib.com \n\n- [Twitter](https://twitter.com) \n- [Facebook](https://facebook.com) \n- [Instagram](https://instagram.com)""")

def help(user_chat_id):
    bot.send_message(user_chat_id, """Check out our FAQs for answers to common questions:
    \n[FAQs Page Link]""")


bot.infinity_polling()