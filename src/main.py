import config
import bot

from telegram.ext import Application
from telegram.ext import CommandHandler, MessageHandler, filters


def main():
    cfg = config.Config()

    app = Application.builder().token(cfg.token).build()

    app.add_handler(CommandHandler("start", bot.start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                          bot.echo))

    
    print("Bot en marcha")
    app.run_polling()

if __name__ == '__main__':
    main()
