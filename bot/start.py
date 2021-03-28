# MIT License

# Copyright (c) 2020 カルマ赤羽 // This file is part of Chitanda

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from telegram import (Update, ParseMode, InlineKeyboardMarkup, 
                      InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton )

from telegram.ext import CallbackContext

from bot.String import String


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
            [
                InlineKeyboardButton(text="Commands available ❔",
                                     callback_data="zero_help")
            ],
            [
                InlineKeyboardButton(text="Source",
                                     callback_data="zero_source"),
                InlineKeyboardButton(text="Support",
                                     callback_data="zero_support")
            ]
               ]
    update.message.reply_text(
        String.START_MESSAGE.format(update.message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
        parse_mode=ParseMode.MARKDOWN
        )
