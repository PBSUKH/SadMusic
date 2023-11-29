from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
ਤਕ‌ੜੇ💪 ਮੂਹਰੇ👉 ਕਦੇ ਜੀ ਜੀ🙏 ਨੀ ❌ਕੀਤਾ ਤੇ,ਮਾੜੇ 😡ਨੂੰ ਦੇਖ👀 ਕੇ ਹੱਸਦੇ 😂ਨੀਂ,ਆਪਣੀ ☝🏻🌎ਦੁਨੀਆਂ👉 ਵਿੱਚ ਮਸਤ😎 ਰਹਿੰਦੇ ਆ।ਐਵੇਂ 😏ਕਿਸੇ 👉ਨੂੰ ਦੇਖ 👀ਕੇ ਮੱਚਦੇ 😅ਨੀ,
ਜੋ 👉ਦਿਲ ♥️ਚ ਉਹੀ ਮੂੰਹ 🗣️ਤੇ ਆ,ਤਾਂ 👉ਹੀ ਬਹੁਤਿਆਂ👥 ਨੂੰ ਅਸੀਂ😎 ਜੱਚਦੇ😏 ਨੀ।।
✍🏻 💞 🌷\n\n🏓 𝐌𝐲 𝐑𝐞𝐩𝐨 ➪ **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/ABT_BAD) 💞**\n📡 𝐌𝐚𝐝𝐞 𝐁𝐲 ➪ **[⎯꯭̽🇨🇦꯭꯭ ⃪Вα꯭∂ ꯭мυη∂α_꯭آآ꯭꯭꯭꯭⎯꯭ ꯭̽🌸](https://t.me/II_BAD_MUNDA_II)** 💞
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("🙈𝐀∂∂ 𝐌є🙈", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],

        [
           InlineKeyboardButton("🎵 𝐌υѕι¢ 𝐁σт 🎵", url=f"https://t.me/BAD_BBY_01_BOT")
        ],
        [ 
          InlineKeyboardButton("👻 𝐌αиαgємєит 𝐁σт 👻", url=f"https://t.me/BAD_BBY_02_BOT")
        ],
        [
            InlineKeyboardButton("😈 𝐒тяιиg 𝐁σт 😈", url=f"https://t.me/BAD_STRING_SESSION_BOT")
        ],
        [
            InlineKeyboardButton("☠ 𝐒тяιиg 𝐇α¢к 𝐁σт ☠", url=f"https://t.me/BAD_STRING_SESSION_HACK_BOT")
        ],
        [
            InlineKeyboardButton("🌲 𝐆яσυρ 🌲", url=f"https://t.me/THE_DRAMA_CLUB_01")
        ],
        [
            InlineKeyboardButton("🦋 𝐂нαииєℓ 🦋", url=f"https://t.me/ABT_BAD")
        ],
        [
            InlineKeyboardButton("😎 𝐔ѕтα∂  𝐉ι 😎", url=f"https://t.me/II_BAD_MUNDA_II")
        ]]
            
            
    
        
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/e25a563619c653328830d.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
