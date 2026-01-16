from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,filters, MessageHandler

TOKEN = "8408024860:AAHdwYXOzQsU4ZIbbIfVg3QLMYjNUEt2Wsw"

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message .text.title() == "Siva":
        with open("IMG_20251130_111559_081.jpg", "rb") as img:
            await update.message.reply_photo(photo=img, caption="...........!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("hi", send_image))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_image))

print("Bot is running...")
app.run_polling()
