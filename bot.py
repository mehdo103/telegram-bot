from telegram.ext import Updater, CommandHandler

TOKEN = "توکن_بات_تت"

def start(update, context):
    update.message.reply_text("سلام!")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
