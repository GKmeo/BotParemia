import config as cfg
from telegram     import Update, ForceReply
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import ContextTypes, Application, filters



class Bot:
    app    = None
    config = None


    def __init__(self, cfgfn):
        self.config = cfg.Config(cfgfn)
        self.app = Application.builder().token(self.config.getToken()).build()
        self.addCmdHandlers()
        self.addMsgHandlers()
        print("Bot corriendo")

    def addCmdHandlers(self):
        self.app.add_handler(CommandHandler("start", self.start))

    def addMsgHandlers(self):
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                            self.echo))
    def run(self):
        self.app.run_polling()
        # Para aquí por algún motivo
        print("Bot terminado")

    async def echo(self,
                   update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(update.message.text)
        userId   = update.message.chat.id
        userName = update.message.chat.username
        text     = update.message.text
        print("[{} ({})]: {}".format(userId, userName, text))

    async def start(self,
                    update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )
