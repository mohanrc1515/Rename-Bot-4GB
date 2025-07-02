from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from pyrogram import Client, filters
from helper.database import uploadlimit, usertype

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
    if len(m.command) >= 3:
        try:
            user_id = m.text.split(' ', 2)[1]
            reason = m.text.split(' ', 2)[2]
            await m.reply_text("User Notified Successfully 😁")
            await c.send_message(chat_id=int(user_id), text=reason)
        except:
            await m.reply_text("User Not Notified Successfully 😔")

@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Limit 1GB", callback_data="cp1"),
         InlineKeyboardButton("Disable Account", callback_data="cp2")],
        [InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
    ])
    await message.reply_text("🔧 Account Management", quote=True, reply_markup=button)

@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Yes", callback_data="dft"),
         InlineKeyboardButton("❌ No", callback_data="cancel")]
    ])
    await message.reply_text(
        text="Reset user to default Premium (4GB) plan?",
        quote=True,
        reply_markup=button
    )

# Account management callbacks
@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot, update):
    try:
        id = update.message.reply_to_message.text.split("/ceasepower")
        user_id = id[1].replace(" ", "")
        uploadlimit(int(user_id), 1073741824)  # 1GB
        usertype(int(user_id), "⚠️ Limited")
        await update.message.edit("Account limited to 1GB successfully")
        await bot.send_message(
            user_id,
            f"Your account has been limited to 1GB upload capacity.\n\n"
            f"Contact admin @MadflixOfficials if this was a mistake."
        )
    except Exception as e:
        await update.message.edit(f"Error: {str(e)}")

@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot, update):
    try:
        id = update.message.reply_to_message.text.split("/ceasepower")
        user_id = id[1].replace(" ", "")
        uploadlimit(int(user_id), 0)  # Disable account
        usertype(int(user_id), "❌ Disabled")
        await update.message.edit("Account disabled successfully")
        await bot.send_message(
            user_id,
            f"Your account has been disabled.\n\n"
            f"Contact admin @MadflixOfficials to resolve this."
        )
    except Exception as e:
        await update.message.edit(f"Error: {str(e)}")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot, update):
    try:
        id = update.message.reply_to_message.text.split("/resetpower")
        user_id = id[1].replace(" ", "")
        uploadlimit(int(user_id), 4294967296)  # Reset to default 4GB Premium
        usertype(int(user_id), "Premium")
        await update.message.edit("Account reset to default Premium (4GB) successfully")
        await bot.send_message(
            user_id,
            f"Your account has been reset to default Premium plan with 4GB capacity.\n\n"
            f"You can check your current plan with /myplan"
        )
    except Exception as e:
        await update.message.edit(f"Error: {str(e)}")

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot, update):
    await update.message.edit("Operation cancelled.")
