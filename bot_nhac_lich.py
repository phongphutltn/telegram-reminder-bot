from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio

# === CẤU HÌNH BOT ===
TOKEN = "8071459629:AAFJSEfGjSnalu5qWG7vvSKwHVkUwjZ7VPs"
chat_id = -1002161560087  # Thay sau khi bạn lấy được chat_id của bạn

# Hàm gửi tin nhắn nhắc lịch lúc 7h sáng
async def send_daily_reminder():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🌄 Chào buổi sáng! Đừng quên bắt đầu công việc đúng giờ nhé!"
    )

# Hàm xử lý khi người dùng gõ /start
async def start(update: Update, context):
    await update.message.reply_text("✅ Bot nhắc lịch đã sẵn sàng!")

# Chạy bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Scheduler chạy mỗi ngày lúc 7h sáng
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: asyncio.run(send_daily_reminder()),
                      trigger='cron', hour=7, minute=0)
    scheduler.start()

    print("🤖 Bot đang chạy... sẽ gửi tin nhắn lúc 7h sáng mỗi ngày.")
    app.run_polling()
