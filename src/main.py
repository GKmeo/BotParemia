import util

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola')


def main():
    token = util.readtoken()
    print("token:", token)

    updater = Updater(token)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,
                                          echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
