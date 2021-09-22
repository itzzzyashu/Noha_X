import html
import json 
import random
import requests

from telegram import Update
from telegram.error import BadRequest
from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext
from Cutiepii_Robot import dispatcher, SUPPORT_CHAT
from Cutiepii_Robot.modules.disable import DisableAbleCommandHandler

def cat(update: Update, _):
msg = update.effective_message
pat = requests.get("https://api.thecatapi.com/v1/gifs/search?breed_ids=beng&include_breeds=true").json()
link = cat.get("url")
if not link:
msg.reply_text(f"No URL was received from the API! Please Go To @{SUPPORT_CHAT}")
msg.reply_video(link)

CAT_HANDLER = DisableAbleCommandHandler("cat", cat, run_async=True)

dispatcher.add_handler(CAT_HANDLER)

mod_name = "Cat API"
command_list = [
    "cat",
]
handlers = [
    CAT_HANDLER,
]
