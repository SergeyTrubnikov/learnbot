from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log"
)

PLANETS = {
    "Jupiter": ephem.Jupiter,
    "Mars": ephem.Mars,
    "Mercury": ephem.Mercury,
    "Moon": ephem.Moon,
    "Neptune": ephem.Neptune,
    "Pluto": ephem.Pluto,
    "Saturn": ephem.Saturn,
    "Sun": ephem.Sun,
    "Uranus": ephem.Uranus,
    "Venus": ephem.Venus
}

def get_constellation(bot, update):

    try:
        planet = update.message.text.split()
        if len(planet) > 2:
            update.message.reply_text("Too many arguments: {}. Need: {}".format(len(planet)-1, "1"))
        else:
            planet = planet[1]
            date_format = "%Y/%m/%d"
            curr_date = datetime.date.today().strftime(date_format)
Jupiter
            if planet in PLANETS:
                const = PLANETS[planet](curr_date)
                update.message.reply_text(ephem.constellation(const))
            else:
                 update.message.reply_text("Sorry, I don't know about this planet :( Yet:)")
    except IndexError:
        update.message.reply_text("You didn't type the planet name!")



def greet_user(bot, update):
    text = "Called /start"
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = '''Hello {}! Your typed "{}"'''.format(update.message.chat.first_name, update.message.text)
    logging.info("User %s, Chat ID: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    """The main fucntion for bot"""
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info("Bot is starting")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()

