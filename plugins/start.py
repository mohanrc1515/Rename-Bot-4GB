from datetime import date as date_
import os, re, datetime, random, asyncio, time, humanize
from script import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram import Client, filters, enums
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from helper.progress import humanbytes
from helper.database import botdata, find_one, total_user
from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
from config import *

token = BOT_TOKEN
botid = token.split(':')[0]

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
    
    try:
        id = message.text.split(' ')[1]
    except IndexError:
        id = None

    loading_sticker_message = await message.reply_sticker("CAACAgIAAxkBAALmzGXSSt3ppnOsSl_spnAP8wHC26jpAAJEGQACCOHZSVKp6_XqghKoHgQ")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()
    
    text = f"""Hello {message.from_user.mention} \n\n➻ This Is An Advanced And Yet Powerful Rename Bot.\n\n➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.\n\n➻ You Can Also Convert Video To File Aɴᴅ File To Video.\n\n➻ This Bot Also Supports Custom Thumbnail And Custom Caption.\n\n<b>Bot Is Made By @Madflix_Bots</b>"""
    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates", url="https://t.me/Madflix_Bots"),
        InlineKeyboardButton("💬 Support", url="https://t.me/MadflixBots_Support")],
        [InlineKeyboardButton("🛠️ Help", callback_data='help'),
        InlineKeyboardButton("❤️‍🩹 About", callback_data='about')],
        [InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url="https://t.me/MadflixOfficials")]
        ])
    
    await message.reply_photo(
        photo=START_PIC,
        caption=text,
        reply_markup=button,
        quote=True
        )
    return    

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
        
    user_id = message.from_user.id    
    if FORCE_SUBS:
        try:
            await client.get_chat_member(FORCE_SUBS, user_id)
        except UserNotParticipant:
            await message.reply_text("<b>Hello Dear \n\nYou Need To Join In My Channel To Use Me\n\nKindly Please Join Channel</b>",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup([
                                         [InlineKeyboardButton("🔺 Update Channel 🔺", url=f"https://t.me/{FORCE_SUBS}")]
                                         ]))
            await client.send_message(LOG_CHANNEL, f"<b><u>New User Started The Bot</u></b> \n\n<b>User ID :</b> <code>{user_id}</code> \n<b>First Name :</b> {message.from_user.first_name} \n<b>Last Name :</b> {message.from_user.last_name} \n<b>User Name :</b> @{message.from_user.username} \n<b>User Mention :</b> {message.from_user.mention} \n<b>User Link :</b> <a href='tg://openmessage?user_id={user_id}'>Click Here</a>")
            return
		
    botdata(int(botid))
    bot_data = find_one(int(botid))
    prrename = bot_data['total_rename']
    prsize = bot_data['total_size']
    
    # No flood control checks
    media = await client.get_messages(message.chat.id, message.id)
    file = media.document or media.video or media.audio
    dcid = FileId.decode(file.file_id).dc_id
    filename = file.file_name
    file_id = file.file_id
    
    # Set unlimited access for all users
    uploadlimit(message.from_user.id, 0)  # 0 means unlimited
    usertype(message.from_user.id, "Unlimited")
    
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    total_rename(int(botid), prrename)
    total_size(int(botid), prsize, file.file_size)
    
    await message.reply_text(
        f"""__What Do You Want Me To Do With This File ?__\n\n**File Name :** `{filename}`\n**File Size :** {filesize}\n**DC ID :** {dcid}""", 
        reply_to_message_id=message.id, 
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 Rename", callback_data="rename"),
             InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    )

@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    # Set unlimited access for all users
    uploadlimit(message.from_user.id, 0)  # 0 means unlimited
    usertype(message.from_user.id, "Unlimited")
    
    _newus = find_one(message.from_user.id)
    used = _newus.get("used_limit", 0)
    
    text = f"""<b>🌟 Unlimited Access</b>
┏━━━━━━━━━━━━━━━━━━
┣ <b>User ID:</b> <code>{message.from_user.id}</code>
┣ <b>Name:</b> {message.from_user.mention}
┣ <b>Plan:</b> Unlimited
┗━━━━━━━━━━━━━━━━━━

<b>🚀 Full Features</b>
✓ No File Size Limits
✓ No Daily Upload Limits
✓ Priority Processing
✓ Unlimited Parallel Tasks

<b>📊 Usage Today:</b> {humanbytes(used)}"""

    await message.reply_text(
        text,
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ Close", callback_data="cancel")]])
    )
