import telebot
from decouple import config

BOT_token = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commads=["hello", "help"])
def send_hello_message(msg):
    bot.reply_to(msg,"hello to my bot what you whant?")
    
bot.polling()
