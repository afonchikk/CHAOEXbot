#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import text

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def q1(bot, update):
    #update.message.reply_text(text.q1)
    update.message.reply_text("lalala")
def q2(bot, update):
    update.message.reply_text(text.q2)
def q3(bot, update):
    update.message.reply_text(text.q3)
def q4(bot, update):
    update.message.reply_text(text.q4)
def q5(bot, update):
    update.message.reply_text(text.q5)
def q6(bot, update):
    update.message.reply_text(text.q6)
def q7(bot, update):
    update.message.reply_text(text.q7)
def q8(bot, update):
    update.message.reply_text(text.q8)
def q9(bot, update):
    update.message.reply_text(text.q9)
def q10(bot, update):
    update.message.reply_text(text.q10)
def q11(bot, update):
    update.message.reply_text(text.q11)
def q12(bot, update):
    update.message.reply_text(text.q12)



def start(bot, update):
    """Echo the user message."""
    update.message.reply_text(text.greet_text + text.question_list)

def info(bot, update):
    """Echo the user message."""
    update.message.reply_text(text.greet_text + text.question_list)

def greet(bot, update):
    """Echo the user message."""
    if len(update.message.new_chat_members) > 0:
        new_member_name = ""
        if len(update.message.new_chat_members) == 1:
            new_member_name = update.message.new_chat_members[0]['first_name']
        else:
            new_member_name = "everyone"
        update.message.reply_text("Hello, {}!\n".format(new_member_name) + text.greet_text + text.question_list)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)



def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("643187200:AAH3z8uQZQ-5tuPiN8fbvsXUo7OWNuk2FWk")


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("question_1", q1))
    dp.add_handler(CommandHandler("question_2", q2))
    dp.add_handler(CommandHandler("question_3", q3))
    dp.add_handler(CommandHandler("question_4", q4))
    dp.add_handler(CommandHandler("question_5", q5))
    dp.add_handler(CommandHandler("question_6", q6))
    dp.add_handler(CommandHandler("question_7", q7))
    dp.add_handler(CommandHandler("question_8", q8))
    dp.add_handler(CommandHandler("question_9", q9))
    dp.add_handler(CommandHandler("question_10", q10))
    dp.add_handler(CommandHandler("question_11", q11))
    dp.add_handler(CommandHandler("question_12", q12))



    # greet new member
    dp.add_handler(MessageHandler(None, greet))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
