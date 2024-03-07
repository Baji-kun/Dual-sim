import asyncio
from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime, timedelta

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    uptime = get_readable_uptime(bot.uptime)
    await message.reply(BOT_STATS_TEXT.format(uptime=uptime))

@Bot.on_message(filters.private)
async def reply_to_private_messages(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
        await asyncio.sleep(30)
