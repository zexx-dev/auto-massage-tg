from pyrogram import Client, filters
from config import ADMIN_ID
import json

DB_FILE = "database.json"

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

@Client.on_message(filters.command("settext") & filters.user(ADMIN_ID))
async def set_text(client, message):

    if len(message.command) < 2:
        return

    text = message.text.split(None, 1)[1]

    data = load_db()

    data["text"] = text

    save_db(data)

    await message.reply("✅ Text Saved")

@Client.on_message(filters.photo & filters.user(ADMIN_ID))
async def save_photo(client, message):

    data = load_db()

    path = await message.download(file_name="photo.jpg")

    data["photo"] = path

    save_db(data)

    await message.reply("✅ Photo Saved")

@Client.on_message(filters.video & filters.user(ADMIN_ID))
async def save_video(client, message):

    data = load_db()

    path = await message.download(file_name="video.mp4")

    data["video"] = path

    save_db(data)

    await message.reply("✅ Video Saved")

@Client.on_message(filters.document & filters.user(ADMIN_ID))
async def save_apk(client, message):

    if not message.document.file_name.endswith(".apk"):
        return

    data = load_db()

    path = await message.download(file_name="app.apk")

    data["apk"] = path

    save_db(data)

    await message.reply("✅ APK Saved")