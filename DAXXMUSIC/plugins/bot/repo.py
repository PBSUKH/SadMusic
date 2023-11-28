from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
ਤਕ‌ੜੇ💪 ਮੂਹਰੇ👉 ਕਦੇ ਜੀ ਜੀ🙏 ਨੀ ❌ਕੀਤਾ ਤੇ,ਮਾੜੇ 😡ਨੂੰ ਦੇਖ👀 ਕੇ ਹੱਸਦੇ 😂ਨੀਂ,ਆਪਣੀ ☝🏻🌎ਦੁਨੀਆਂ👉 ਵਿੱਚ ਮਸਤ😎 ਰਹਿੰਦੇ ਆ।ਐਵੇਂ 😏ਕਿਸੇ 👉ਨੂੰ ਦੇਖ 👀ਕੇ ਮੱਚਦੇ 😅ਨੀ,
ਜੋ 👉ਦਿਲ ♥️ਚ ਉਹੀ ਮੂੰਹ 🗣️ਤੇ ਆ,ਤਾਂ 👉ਹੀ ਬਹੁਤਿਆਂ👥 ਨੂੰ ਅਸੀਂ😎 ਜੱਚਦੇ😏 ਨੀ।।
✍🏻 💞\n📡 𝐌𝐚𝐝𝐞 𝐁𝐲 ➪ [⎯꯭‌🇨🇦꯭꯭ ⃪Вα꯭∂ ꯭мυη∂α_꯭آآ꯭꯭꯭꯭⎯꯭ ꯭‌🌸](https://t.me/II_BAD_MUNDA_II)
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/iam_daxx"),
          ],
               [
                InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url=f"https://t.me/ALLTYPECC"),

],
[
              InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://github.com/DAXXTEAM/DAXXBANALL"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/DAXXTEAM/DAXXMUSIC"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com/DAXXTEAM/YumikooRobot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXCHATBOT"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXSTRINGBOT"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://github.com/DAXXTEAM/DAXXCHATGPT"),
],
[
              InlineKeyboardButton("𝗩𝗣𝗦", url=f"https://github.com/DAXXTEAM/Kaali-Linux"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com/DAXXTEAM/DAXXMOVIEBOT"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://github.com/DAXXTEAM/DAXXSTRINGHACK"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXIDCHAT"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/DAXXUSERBOT"),
InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/SEARCH_BOT"),
],
[
InlineKeyboardButton("𝗖𝗖 𝗕𝗢𝗧", url=f"https://github.com/DAXXTEAM/CC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/faa1f3ad7116e33d9f402.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
