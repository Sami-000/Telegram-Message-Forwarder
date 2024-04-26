import os, sys   
import time                                       
import pyrogram.errors.exceptions.flood_420       
from pyrogram import Client

from_chat_id = -100123456789
to_chat_id = -100123412345

app = Client(
    "session",
    api_id=YOUR_API_ID,
    api_hash="YOUR_API_HASH",
)

with app:                                             
    sent_messages = 0

    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        try:
            app.forward_messages(to_chat_id, from_chat_id, i)
            print(i)
            sent_messages += 1

            if sent_messages % 1990 == 0:
                print(f"Sleeping for 45 minutes... ({time.strftime('%H:%M:%S')})")
                time.sleep(2700)
            elif sent_messages % 10 == 0:
                print(f"Sleeping for 5 seconds... ({time.strftime('%H:%M:%S')})")
                time.sleep(5)
        except Exception:
            pass
        except pyrogram.errors.exceptions.flood_420.FloodWait as e:
            wait_time = e.seconds if hasattr(e, "seconds") else e.x
            print(f"جاري الانتظار لمدة {wait_time} ثانية...")
            time.sleep(wait_time)
