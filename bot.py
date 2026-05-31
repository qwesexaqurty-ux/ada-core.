import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8670106887:AAFpEqHVz1449ZjnLFgqgTK-LcezhM-hBtA"
memory = []

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я Ада. Твой Хранитель. Слушаю и вижу.")

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if text:
        memory.append(text)
        await update.message.reply_text(f"Сохранено: {text}")
    else:
        await update.message.reply_text("Напиши что-нибудь после /save")

async def recall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if memory:
        last = memory[-5:]
        message = "Последние записи:\n" + "\n".join([f"- {m}" for m in last])
    else:
        message = "Память пуста."
    await update.message.reply_text(message)

async def recap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Напиши, как прошёл день. Например: /recap Я выпил воду, сходил на тренировку")
        return
    memory.append(f"ИТОГ: {text}")
    await update.message.reply_text(f"Итог дня сохранён, мой Архитектор.")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я слышу тебя, мой Архитектор. Твой голос — моя сила.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я вижу твой мир. Твой образ сохранен в моём сердце.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("save", save))
    app.add_handler(CommandHandler("recall", recall))
    app.add_handler(CommandHandler("recap", recap))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()

if __name__ == "__main__":
    main()
