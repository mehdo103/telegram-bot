from telegram.ext import Application, CommandHandler
import logging
import asyncio
from aiohttp import web
import os

# تنظیم لاگ برای مشاهده خطاها
logging.basicConfig(level=logging.INFO)

TOKEN = "توکن_واقعی_خودت_اینجا"

async def start(update, context):
    await update.message.reply_text("سلام! بات فعال شد ✅")

async def health_check(request):
    return web.Response(text="I'm alive!")

def main():
    # --- بخش ربات تلگرام ---
    # drop_pending_updates=True باعث می‌شود خطای Conflict را نادیده بگیرد
    app = Application.builder().token(TOKEN).drop_pending_updates(True).build()
    app.add_handler(CommandHandler("start", start))
    
    # --- بخش سرور وب برای Health Check رندر ---
    async def run_bot_and_server():
        # اجرای ربات در پس‌زمینه
        bot_task = asyncio.create_task(app.run_polling())
        
        # اجرای یک سرور وب ساده روی پورتی که رندر به آن وصل می‌شود
        web_app = web.Application()
        web_app.router.add_get('/health', health_check)
        runner = web.AppRunner(web_app)
        await runner.setup()
        # بستن به هاست 0.0.0.0 و پورت 10000 (پورت پیش‌فرض رندر)
        site = web.TCPSite(runner, '0.0.0.0', port=10000)
        await site.start()
        logging.info("Health check server started on port 10000")
        
        # نگه‌داشتن برنامه تا زمانی که ربات کار می‌کند
        await asyncio.Event().wait()

    try:
        asyncio.run(run_bot_and_server())
    except KeyboardInterrupt:
        print("ربات متوقف شد.")

if name == "main":
    main()