
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n┃ Developer : <a href='tg://user?id={5971676967}'>Siam Chowdhury</a>\n┃ Creator : <a href='tg://user?id=https://t.me/Chowdhury_Siam'> This Person </a>\n┃ Language : <code>Python3</code>\n┃ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n┃ Source Code : <a href=https://t.me/Chowdhury_Siam>Contact Me</a>\n┃ Main Channel : <a href=https://t.me/Anime_Kun_Channel>​Anime Kun</a>\n┃ Chat Group : <a href=https://t.me/AnimeKunChannel>Anime Kun GC</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Close Me", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
