import os
import logging
import asyncio
from aiohttp import web
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تنظیم لاگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# گرفتن توکن از محیط
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    logger.error("BOT_TOKEN تنظیم نشده!")
    exit(1)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات آنلاین است ✅")

# صفحه سلامت برای رندر
async def health_check(request):
    return web.Response(text="OK", status=200)

async def main():
    # راه‌اندازی ربات
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # راه‌اندازی سرور وب برای health check
    web_app = web.Application()
    web_app.router.add_get("/", health_check)
    web_app.router.add_get("/health", health_check)
    
    runner = web.AppRunner(web_app)
    await runner.setup()
    
    # استفاده از پورت محیط یا ۱۰۰۰۰
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    logger.info(f"ربات و سرور وب روی پورت {port} راه‌اندازی شدند!")
    
    # اجرای همزمان ربات و سرور
    await asyncio.gather(
        app.run_polling(),
        asyncio.Event().wait()  # سرور رو روشن نگه می‌داره
    )

if __name__ == "__main__":
    asyncio.run(main())
