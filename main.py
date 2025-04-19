import telebot

# Remplace ce token par le tien
TOKEN = "7539796870:AAFNBwA7NSDQGnvGd9LE5wyF47wfiJntJ54"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salut, je suis YvesTrader, ton assistant IA de trading !")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Je suis en ligne, prêt à t'aider avec le marché.")

bot.polling()
