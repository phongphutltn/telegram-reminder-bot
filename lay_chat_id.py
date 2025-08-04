import telebot

API_TOKEN = '8071459629:AAFJSEfGjSnalu5qWG7vvSKwHVkUwjZ7VPs'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def get_chat_id(message):
    print("Chat ID:", message.chat.id)
    print("Tên:", message.chat.title or message.chat.username or message.chat.first_name)
    print("Loại:", message.chat.type)

bot.polling()
