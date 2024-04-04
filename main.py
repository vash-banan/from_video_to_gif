from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7045425968:AAFXlF9K-5GXLiO_hbWKmQIP-mG0YXGb6vk'
BOT_USERNAME : Final = '@From_video_to_gif_bot'

#команда вызывается когда пользователь нажмет на /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здравствуй этот бот создан для конвертирования видео в gif.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Вот команды которые вы можете использовать')



#логика

def handle_response(text: str) -> str:
    text_lower: str = text.lower()
    
    if '!hello' in text_lower:
        return 'команды:'
    
    ...

    return 'Вот команды которые вы можете использовать'