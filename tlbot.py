import telebot
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commads=["start", "help"])
def send_start_message(msg):
    bot.reply_to(msg, "hello to my bot what you whant?")
    
bot.polling()
