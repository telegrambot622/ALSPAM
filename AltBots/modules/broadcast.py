import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, CMD_HNDLR as hl

from telethon import events


mongo_client = AsyncIOMotorClient("mongodb+srv://yashsamrat32169:ylWiINR00JzSqwhP@cluster0.j44oov2.mongodb.net/?retryWrites=true&w=majority")
mongodb = mongo_client.get_default_database()

async def count_groups(client):
    count = 0
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            count += 1
    return count

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
async def stats(legend):
    if legend.sender_id == OWNER_ID:
        users = await legend.client.get_me()
        groups_count = await count_groups(legend.client)
        await legend.reply(f"Current users: {users.total_count}\nActive in {groups_count} groups.")
    else:
        await legend.reply("Sorry, only the bot owner can access this command.")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
async def broadcast(legend):
    if legend.sender_id == OWNER_ID:
        groups_count = await count_groups(legend.client)
        await legend.reply(f"Broadcasting message to {groups_count} groups...")
        
    else:
        await legend.reply("Sorry, only the bot owner can access this command.")
