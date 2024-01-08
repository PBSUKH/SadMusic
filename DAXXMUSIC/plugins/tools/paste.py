from asyncio import get_running_loop, sleep, TimeoutError
from functools import partial
from DAXXMUSIC import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import ClientSession
import re
import os
import socket
import aiofiles
import aiohttp
import asyncio
from io import BytesIO

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image
    
aiohttpsession = ClientSession()

# Rest of your code remains unchanged...

def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()

async def paste(content):
    loop = get_running_loop()
    link = await loop.run_in_executor(None, partial(_netcat, "ezup.dev", 9999, content))
    return link

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with aiohttpsession.head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return status == 200
    return False

@app.on_message(filters.command("paste"))
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ /paste**")
    m = await message.reply_text("**ᴘᴀsᴛɪɴɢ ᴘʟs ᴡᴀɪᴛ 10 sᴇᴄ....**")
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴘᴀsᴛᴇ ғɪʟᴇs sᴍᴀʟʟᴇʀ ᴛʜᴀɴ 1ᴍʙ.**")
        if not pattern.search(document.mime_type):
            return await m.edit("**ᴏɴʟʏ ᴛᴇxᴛ ғɪʟᴇs ᴄᴀɴ ʙᴇ ᴘᴀsᴛᴇᴅ.**")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
        carbon = await make_carbon(content)
        await m.delete()
        text = await message.reply("**✍️ᴘᴀsᴛᴇᴅ ᴏɴ ᴄᴀʀʙᴏɴ ᴘᴀɢᴇ !**")
        await asyncio.sleep(0.4)
        await text.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ ᴜɴᴅᴇʀ 5 sᴇᴄ.**")
        await asyncio.sleep(0.4)
        await text.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ ᴜɴᴅᴇʀ 5 sᴇᴄ....**")
        await message.reply_photo(carbon)
        await text.delete()
        carbon.close()
    
