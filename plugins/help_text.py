#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anand PS Kerala

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation
from .thuppakki import thupaki

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
def help_user(bot, update):
    # logger.info(update)
    keyboard = [[pyrogram.InlineKeyboardButton(text="Thuppakki", callback_data=thupaki)]]
    TRChatBase(update.from_user.id, update.text, "/help")
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup = pyrogram.InlineKeyboardMarkup(keyboard),
        reply_to_message_id=update.message_id
    )



@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )

