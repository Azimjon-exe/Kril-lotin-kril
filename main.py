import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "1867937057:AAFXkVPn_MasJAGIpO-7LZ--i_T8_BKgOf8"
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f'Assalom alaykum, {username} IT Uz Life kanalining Lotin kiril, Kril Lotin botiga Xush kelibsiz!'
    xabar += '\nMatningizni yuboring: '
    bot.reply_to(message, xabar)

# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))
    

bot.polling()

