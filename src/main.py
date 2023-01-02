import util

from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.ext import MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)
    print(update.message.text)


def main():
    token = util.readtoken()
    print("token:", token)

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                          echo))

    app.run_polling()

if __name__ == '__main__':
    main()
