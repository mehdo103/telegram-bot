from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 من ربات شما هستم")

app = Application.builder().token("8827451419:AAFnsbvId6Ac4gnxNyhJITdKbVgP9t8HgxY").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()