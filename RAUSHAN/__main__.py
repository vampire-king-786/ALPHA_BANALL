import os
import logging
from config import BOT_USERNAME
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
    filters.command("start")
    & filters.private
)
async def start_command(client, message: Message):
    user = message.from_user
    await message.reply_photo(
        photo=f"https://files.catbox.moe/em1qox.jpg",
        caption=f"✦ » ʜᴇʏ {user.mention}\n✦ » ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙʀᴀʀʏ.\n\n✦ » ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs.\n\n**✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ ɢɪᴠᴇ ᴍᴇ ғᴜʟʟ ᴘᴏᴡᴇʀs ᴀɴᴅ ᴛʏᴘᴇ /banall ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.**✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ »  <a href=t.me/lllVAMPIRE_KINGlll>⎯᪵፝֟፝❍⏤‌‌𝗩𝗔𝗠𝗣𝗜𝗥𝗘 𝗞𝗜𝗡𝗚乛|⁪⁬⁮⁮⁮⁮𓆩〭〬🔥𓆪ꪾ™ </a>a>**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜️ Aᴅᴅ ᴍᴇ Bᴀʙʏ ⚜️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton("🔸 ❍ᴡɴᴇʀ🔸", url="http://t.me/lllVAMPIRE_KINGlll"),
                    InlineKeyboardButton("▫️ 𝗨ᴘᴅᴀᴛᴇs ▫️", url="https://t.me/VAMPIRE_UPDATESS")
                ]                
            ]
        )
    )

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
