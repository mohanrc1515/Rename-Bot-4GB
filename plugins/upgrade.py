from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):
    text = """**🌟 Premium Plan Features (Default for All Users)**
✓ Upload 4GB Files
✓ Daily Upload Limit: 4GB
✓ High Priority Processing
✓ 0 Second Timeout
✓ Unlimited Parallel Processes
✓ Time Gap Support

**💎 Enhanced Plans (Optional Upgrades)**
**🪙 Basic+**
Daily Upload Limit: 20GB
Price: Rs 49 / $0.59 per Month

**⚡ Standard+**
Daily Upload Limit: 50GB 
Price: Rs 99 / $1.19 per Month

**🚀 Pro+**
Daily Upload Limit: 100GB
Price: Rs 179 / $2.16 per Month

Payment Details:
<b>➜ UPI ID:</b> <code>madflixofficial@axl</code>
<b>➜ PayPal:</b> <a href='https://www.paypal.me/jishudeveloper'>Click Here</a>
<b>➜ QR Code:</b> <a href='https://telegra.ph/QR-Payment-07-24-4'>Click Here</a>

After payment, send screenshots to @MadflixOfficials"""
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Contact Admin", url="https://t.me/calladminrobot"),
         InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    
    await update.message.edit(text=text, reply_markup=keyboard, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):
    text = """**🌟 Premium Plan Features (Default for All Users)**
✓ Upload 4GB Files
✓ Daily Upload Limit: 4GB
✓ High Priority Processing
✓ 0 Second Timeout
✓ Unlimited Parallel Processes
✓ Time Gap Support

**💎 Enhanced Plans (Optional Upgrades)**
**🪙 Basic+**
Daily Upload Limit: 20GB
Price: Rs 49 / $0.59 per Month

**⚡ Standard+**
Daily Upload Limit: 50GB 
Price: Rs 99 / $1.19 per Month

**🚀 Pro+**
Daily Upload Limit: 100GB
Price: Rs 179 / $2.16 per Month

Payment Details:
<b>➜ UPI ID:</b> <code>madflixofficial@axl</code>
<b>➜ PayPal:</b> <a href='https://www.paypal.me/jishudeveloper'>Click Here</a>
<b>➜ QR Code:</b> <a href='https://telegra.ph/QR-Payment-07-24-4'>Click Here</a>

After payment, send screenshots to @MadflixOfficials"""
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Contact Admin", url="https://t.me/calladminrobot"),
         InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    
    await message.reply_text(text=text, reply_markup=keyboard, quote=True, disable_web_page_preview=True)
