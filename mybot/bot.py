import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime



logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    print("Вызван/start")
    update.message.reply_text("Приветствую, пользователь!")

def talk_to_me(update, context):

    text = update.message.text
    planet_name = text.split()[-1]

    if planet_name == 'Mars':
       mars= ephem.Mars()
       mars.compute(ephem.Date(datetime.date.today()))
       result = ephem.constellation(mars)
       update.message.reply_text(result)
    
    if planet_name == 'Jupiter':
        jupiter = ephem.Jupiter()
        jupiter.compute(ephem.Date(datetime.date.today()))
        result = ephem.constellation(jupiter)
        update.message.reply_text(result)
    
    if planet_name == 'Mercury':
        mercury = ephem.Mercury()
        mercury.compute(ephem.Date(datetime.date.today()))
        result = ephem.constellation(mercury)
        update.message.reply_text(result)    
    
    else:
      print(text)
      update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))



    logging.info("Bot is running!")
    mybot.start_polling()
    mybot.idle()

if __name__=='__main__':
  main()