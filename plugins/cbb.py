#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐂𝗋𝖾α𝗍ⱺ𝗋 : <a href='tg://user?id=OWNER_ID >This Person</a>\n○ 𝐋α𐓣𝗀υα𝗀𝖾 : <code>𝐏𝗒𝗍ɦⱺ𐓣3</code>\n○ 𝐋𝗂ᑲ𝗋α𝗋𝗒 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 𝐂ɦα𐓣𐓣𝖾ᥣ : @Movies_hunnt\n○ 𝐒υρρⱺ𝗋𝗍 𝐆𝗋ⱺυρ : @INDIAN_HACKER_GROUP</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝐂ᥣⱺ𝗌𝖾", callback_data = "close")
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
