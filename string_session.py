
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
PROUD-INDIAN-BOT = """
"""
print(PROUD-INDIAN-BOT)
print("""String Generator. ==> PROUD-INDIAN-BOT. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.

APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as PROUD-INDIAN-BOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(PROUD-INDIAN-BOT.session.save())
    print("")
    print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
    omk =PROUD-INDIAN-BOT.send_message("me", f"`{PROUD-INDIAN-BOT.session.save()}`")
    omk.reply("The above is the `StonedLegend_STRING` #POWERFUL [PROUD-INDIAN-BOT](https://t.me/Proud-Indian-bot)"
		)
