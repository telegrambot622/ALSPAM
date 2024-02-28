import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from os import execl, getenv
from telethon import events
from datetime import datetime

def get_client_list():
    return [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

async def get_stats():
    total_chats = await X1.get_dialogs_count()
    return f"Total chats: {total_chats}"

async def get_group_count():
    total_groups = await X1.get_dialogs_count()
    return f"Total groups: {total_groups}"

def disconnect_clients():
    for client in get_client_list():
        try:
            client.disconnect()
        except Exception:
            pass

def update_sudo_users(newsudo):
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
    heroku_var["SUDO_USERS"] = newsudo

@events.register(events.NewMessage)
async def sudo_operations(event):
    if event.sender_id == OWNER_ID:
        if event.text.startswith(f"{hl}sudolist"):
            sudousers = getenv("SUDO_USERS", default=None)
            if sudousers:
                await event.reply(f"» 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂:\n{sudousers}")
            else:
                await event.reply("» 𝙽𝙾 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂 𝙾𝙽 𝚃𝙷𝙴 𝙱𝙾𝚃.")
        
        elif event.text.startswith(f"{hl}removesudo"):
            try:
                reply_msg = await event.get_reply_message()
                target = reply_msg.sender_id
            except:
                await event.reply("» 🌺𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁🌺 !!")
                return
            sudousers = getenv("SUDO_USERS", default=None)
            if str(target) in sudousers:
                newsudo = sudousers.replace(str(target), "").strip()
                update_sudo_users(newsudo)
                await event.reply(f"» 𝙾𝚇𝚈𝙶𝙴𝙽 𝚄𝚂𝙴𝚁 𝚁𝙴𝙼𝙾𝚅𝙴𝙳\n\n🛠️ 𝙽𝙴𝚆 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂: {newsudo} 🛠️")
            else:
                await event.reply("» 🌸𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙽𝙾𝚃 𝙰 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁🌸 !!")
        
        elif event.text.startswith(f"{hl}stats"):
            stats = await get_stats()
            await event.reply(stats)

        elif event.text.startswith(f"{hl}groupcount"):
            group_count = await get_group_count()
            await event.reply(group_count)

        elif event.text.startswith(f"{hl}broadcast"):
            try:
                message = event.text.split(" ", 1)[1]
                for client in get_client_list():
                    await client.send_message("me", message)
                await event.reply("» 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈.")
            except IndexError:
                await event.reply("» 🌺𝙿𝙻𝙴𝙰𝚂𝙴 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴🌺.")

@events.register(events.NewMessage)
async def sudo_commands(event):
    if event.sender_id in SUDO_USERS:
        if event.text.startswith(f"{hl}ping"):
            start = datetime.now()
            altron = await event.reply(f"» ™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍")
            end = datetime.now()
            mp = (end - start).microseconds / 1000
            await altron.edit(f"💫🥀 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍\n» {mp} 𝙼𝚂")
        
        elif event.text.startswith(f"{hl}reboot"):
            await event.reply(f"🥀𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙾𝚇𝚈𝙶𝙴𝙽 𝐁𝐎𝐓𝐒🥀...")
            disconnect_clients()
            execl(sys.executable, sys.executable, *sys.argv)
        
        elif event.text.startswith(f"{hl}sudo"):
            try:
                reply_msg = await event.get_reply_message()
                target = reply_msg.sender_id
            except:
                await event.reply("» 🌺𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁🌺 !!")
                return
            sudousers = getenv("SUDO_USERS", default=None)
            if str(target) in sudousers:
                await event.reply("» 🌸𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙰 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙾𝙵 𝙾𝚇𝚈𝙶𝙴𝙽 𝙱𝙾𝚃𝚂🌸 !!")
            else:
                newsudo = f"{sudousers} {target}" if len(sudousers) > 0 else f"{target}"
                update_sudo_users(newsudo)
                await event.reply(f"» 𝙽𝙴𝚆 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁: {target}\n» 💖𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙾𝚇𝚈𝙶𝙴𝙽 𝙱𝙾𝚃𝚂💖...")
        
