
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n┃ Developer : <a href='https://t.me/Itz_Zeno'>Zeno</a>\n┃ Creator : <a href='https://t.me/Itz_Zeno'> This Person </a>\n┃ Language : <code>Python3</code>\n┃ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n┃ Source Code : <a href=https://t.me/Netflix_Dual>Movie Channel</a>\n┃ Main Channel : <a href=https://t.me/Anime_Wide>​Anime Wide</a>\n┃Request Gc: <a href=https://t.me/Series_and_Movies_Request_Group>Series & Movies Gc</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
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
