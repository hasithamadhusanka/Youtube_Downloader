# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : Youtube_Downloader 'Inline' [ Telegram ]
# Repo     : https://github.com/Rexinazor/Youtube_Downloader
# Author   : Hasitha Madhushanka

from urllib.parse import quote
from presets import Presets
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = [
    [
        InlineKeyboardButton('View Thumb', callback_data='view_btn'),
        InlineKeyboardButton('Del Thumb', callback_data='del_btn')

    ],
    [
        InlineKeyboardButton('Help', callback_data='help_btn'),
        InlineKeyboardButton('Search Inline', switch_inline_query_current_chat='')
    ]
]


del_thumb = [
    [
        InlineKeyboardButton("DEL THUMB", callback_data="thumb_del_conf_btn"),
        InlineKeyboardButton("Back", callback_data="a_back_btn")
    ]
]

join_channel = [
    [
        InlineKeyboardButton('⚙ Join Updates', url='https://telegram.me/BioHazard_Bots'),
        InlineKeyboardButton('Search Inline', switch_inline_query_current_chat='')
    ]
]


back_button = [
    [
        InlineKeyboardButton('⬅️ Back', callback_data='back_btn')
    ]
]

close_button = [
    [
        InlineKeyboardButton('❌ Close', callback_data='close_btn'),
        InlineKeyboardButton('Home', callback_data='home_btn')
    ]
]

cancel_button = [
    [
        InlineKeyboardButton('Cancel', callback_data='cancel_btn')
    ]
]

reply_markup_cancel = InlineKeyboardMarkup(cancel_button)
reply_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_join = InlineKeyboardMarkup(join_channel)
reply_markup_del_thumb = InlineKeyboardMarkup(del_thumb)
reply_markup_start = InlineKeyboardMarkup(start_btn)

def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Presets.SHARE_BUTTON_TEXT.format(username=username))
    buttons = [[InlineKeyboardButton('Share bot', url=url),
                InlineKeyboardButton("Search Inline", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share
