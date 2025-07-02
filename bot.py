from pyrogram import Client, idle
from pyrogram.errors import FloodWait, RPCError
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
import asyncio
import time
import sys

# Set minimum chat IDs
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

async def start_bots():
    # Initialize the main bot
    bot = Client(
        "Renamer",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root='plugins'),
        workers=100  # Increased worker count for better performance
    )

    try:
        # Start the main bot
        await bot.start()
        print("✅ Main bot started successfully!")
        
        # Start userbot if STRING_SESSION exists
        if STRING_SESSION:
            try:
                await Client2.start()
                print("✅ Userbot client started successfully!")
            except Exception as e:
                print(f"❌ Failed to start userbot: {e}")
                Client2 = None

        # Keep the bots running
        await idle()

    except FloodWait as e:
        print(f"⏳ FloodWait: Need to wait {e.value} seconds")
        time.sleep(e.value + 5)  # Wait required time plus buffer
        await start_bots()  # Restart after waiting
    except RPCError as e:
        print(f"⚠️ RPC Error: {e}")
        time.sleep(10)
        await start_bots()  # Restart after short delay
    except Exception as e:
        print(f"❌ Critical error: {e}")
    finally:
        # Proper cleanup
        print("🛑 Stopping bots...")
        try:
            await bot.stop()
            if STRING_SESSION and Client2:
                await Client2.stop()
        except:
            pass
        sys.exit(0)

if __name__ == "__main__":
    # Set proper event loop policy for Windows if needed
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Run with proper error handling
    while True:
        try:
            asyncio.run(start_bots())
        except KeyboardInterrupt:
            print("🛑 Received exit signal, shutting down...")
            break
        except Exception as e:
            print(f"🔄 Restarting due to error: {e}")
            time.sleep(5)
