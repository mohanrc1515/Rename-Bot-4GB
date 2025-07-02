@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    # Set all users to unlimited access by default
    uploadlimit(message.from_user.id, 0)  # 0 means unlimited
    usertype(message.from_user.id, "Unlimited")
    
    _newus = find_one(message.from_user.id)
    used = _newus.get("used_limit", 0)
    
    text = f"""<b>🌟 Account Information</b>
┏━━━━━━━━━━━━━━━━━━
┣ <b>User ID:</b> <code>{message.from_user.id}</code>
┣ <b>Name:</b> {message.from_user.mention}
┣ <b>Plan:</b> Unlimited Access
┗━━━━━━━━━━━━━━━━━━

<b>🚀 Full Features Available</b>
✓ Unlimited File Uploads
✓ No Size Restrictions
✓ Instant Processing
✓ Unlimited Parallel Tasks
✓ No Daily Limits
✓ Priority Support

<b>📊 Usage Today:</b> {humanbytes(used)}"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    
    await message.reply(
        text=text,
        quote=True,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )
