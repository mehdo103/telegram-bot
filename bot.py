from telegram.ext import Application, CommandHandler

TOKEN = "8827451419:AAEiywLVxGL1Bsdd-RpnY_U-SGue3kOmHeo"

async def start(update, context):
    await update.message.reply_text("سلام! بات فعال شد ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("بات روشن شد...")
    app.run_polling()

if __name__ == "__main__":
    main()
