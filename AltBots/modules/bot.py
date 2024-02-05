@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sremsudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __𝚁𝙴𝙼𝙾𝚅𝙸𝙽𝙶 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁💔...__🚀🚀")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» 🌺𝙽𝙾 𝚂𝚄𝙳𝙾 𝚃𝙾 𝚁𝙴𝙼𝙾𝚅𝙴🌺 !!")
            return

        if str(target) not in sudousers:
            await ok.edit("» 🌸𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙽𝙾𝚃 𝙰 𝚂𝚄𝙳𝙾 𝙄𝚂𝙴𝚁 𝙾𝚁 𝙾𝚇𝚈𝙶𝙴𝙽 𝙱𝙾𝚃🌸 !!")
        else:
            sudousers_list = sudousers.split(" ")
            sudousers_list.remove(str(target))
            newsudo = " ".join(sudousers_list)
            await ok.edit(f"» **𝙽𝙴𝚆 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁**: `{target}`\n» 💔𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁💔...`")
            heroku_var["SUDO_USERS"] = newsudo

    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝚂𝙾𝚁𝚁𝚈, 𝙾𝙽𝙻𝚈 𝙾𝚆𝙽𝙴𝚁 𝙲𝙰𝙽 𝙰𝙲𝙴𝚂𝚂 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def sudolist(event):
    if event.sender_id == OWNER_ID:
        sudousers = getenv("SUDO_USERS", default=None)

        if sudousers:
            sudousers_list = sudousers.split(" ")
            msg = "» 💖 **𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃** 💖\n\n"
            for index, user_id in enumerate(sudousers_list, start=1):
                msg += f"{index}. `{user_id}`\n"
            await event.reply(msg)
        else:
            await event.reply("» 🌺 **𝙽𝙾 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈** 🌺")

    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝚂𝙾𝚁𝚁𝚈, 𝙾𝙽𝙻𝚈 𝙾𝚆𝙽𝙴𝚁 𝙲𝙰𝙽 𝙰𝙲𝙴𝚂𝚂 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.")
