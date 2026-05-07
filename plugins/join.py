from pyrogram import Client
from pyrogram.types import ChatJoinRequest
import json

DB_FILE = "database.json"

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

@Client.on_chat_join_request()
async def auto_accept(client, join_request):

    user_id = join_request.from_user.id

    await join_request.approve()

    data = load_db()

    try:

        if data["text"]:
            await client.send_message(user_id, data["text"])

        if data["photo"]:
            await client.send_photo(user_id, data["photo"])

        if data["video"]:
            await client.send_video(user_id, data["video"])

        if data["apk"]:
            await client.send_document(user_id, data["apk"])

    except Exception as e:
        print(e)