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
    ]
    [
        [ 
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url=f"https://t.me/II_BAD_MUNDA_II")
        ],
    ]
        
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/e25a563619c653328830d.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
