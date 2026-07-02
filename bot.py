from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧪 سلام!\n\nبه ربات انجمن علمی شیمی خوش اومدی 🌸"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("ربات روشن شد...")

app.run_polling()