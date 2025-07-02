@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    used_ = find_one(message.from_user.id)
    daily = used_["daily"]
    expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
    if expi != 0:
        today = date_.today()
        pattern = '%Y-%m-%d'
        epcho = int(time.mktime(time.strptime(str(today), pattern)))
        daily_(message.from_user.id, epcho)
        used_limit(message.from_user.id, 0)
    
    # Force all users to Premium with 4GB limit
    uploadlimit(message.from_user.id, 4294967296)  # 4GB in bytes
    usertype(message.from_user.id, "Premium")
    
    _newus = find_one(message.from_user.id)
    used = _newus["used_limit"]
    limit = _newus["uploadlimit"]
    remain = int(limit) - int(used)
    ends = _newus["prexdate"]
    
    normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d') if ends else "Lifetime"
    
    text = f"""<b>📊 Account Details</b>
┏━━━━━━━━━━━━━━
┣⪼ <b>User ID:</b> <code>{message.from_user.id}</code>
┣⪼ <b>Name:</b> {message.from_user.mention}
┣⪼ <b>Plan:</b> Premium (Default)
┗━━━━━━━━━━━━━━

<b>🚀 Current Plan Features</b>
✓ 4GB File Uploads
✓ Daily Limit: {humanbytes(limit)}
✓ Used Today: {humanbytes(used)}
✓ Remaining: {humanbytes(remain)}
✓ Instant Processing
✓ Unlimited Parallel Tasks

<b>⏳ Plan Status:</b> {normal_date}

<i>You can upgrade for even higher limits!</i>"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Upgrade Plans", callback_data="upgrade")],
        [InlineKeyboardButton("✖️ Close", callback_data="cancel")]
    ])
    
    await message.reply(
        text=text,
        quote=True,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )
