from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):

    await message.reply(
        "✅ Bot Active Successfully"
    )