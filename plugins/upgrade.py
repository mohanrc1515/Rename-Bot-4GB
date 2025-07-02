from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):
    text = """**🌟 Unlimited Access For All Users 🌟**

✅ No File Size Limits
✅ No Daily Upload Restrictions  
✅ Priority Processing Speed
✅ Instant Renaming
✅ Unlimited Parallel Tasks
✅ 24/7 Availability

<b>All features are completely free with no limitations!</b>

Need help or have questions?
Contact our support team @MadflixBots_Support"""
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Contact Support", url="https://t.me/MadflixBots_Support")],
        [InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    
    await update.message.edit(
        text=text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):
    text = """**✨ All Features Unlocked ✨**

🔓 No Restrictions
🔓 No Payment Required
🔓 No Premium Tiers

<b>Enjoy these unlimited features:</b>
- Rename files of any size
- Convert between formats freely
- No daily usage limits
- Maximum processing speed

Need assistance? Contact @MadflixBots_Support"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates Channel", url="https://t.me/Madflix_Bots")],
        [InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    
    await message.reply_text(
        text=text,
        reply_markup=keyboard,
        quote=True,
        disable_web_page_preview=True
    )
