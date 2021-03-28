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


import requests
import nekos
import os

from telegram.ext import (CallbackContext,
                          run_async)

from telegram import (ParseMode, Update, InlineKeyboardMarkup, 
                      InlineKeyboardButton, ReplyKeyboardMarkup, 
                      KeyboardButton)

delete_button = 'Delete'


def neko(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "neko"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))
    


def feet(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "feet"
    link = nekos.img(target)    
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def yuri(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "yuri"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def trap(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "trap"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def futanari(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "futanari"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def hololewd(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "hololewd"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def lewdkemo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "lewdkemo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def sologif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "solog"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def feetgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "feetg"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def cumgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "cum"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def erokemo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "erokemo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def lesbian(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "les"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def wallpaper(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "wallpaper"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def lewdk(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "lewdk"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def ngif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "ngif"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def tickle(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "tickle"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def lewd(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "lewd"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def feed(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "feed"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def eroyuri(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "eroyuri"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def eron(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "eron"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def cum(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "cum_jpg"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def bjgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "bj"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def bj(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "blowjob"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def nekonsfw(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "nsfw_neko_gif"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def solo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "solo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def kemonomimi(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "kemonomimi"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def avatarlewd(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def gasm(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def poke(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "poke"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def anal(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "anal"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def hentai(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "hentai"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def avatar(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def erofeet(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "erofeet"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def holo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "holo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


# def keta(update: Update, context: CallbackContext) -> None:
#     msg = update.effective_message
#     target = 'keta'
#     if not target:
#         msg.reply_text("No URL was received from the API!")
#         return
#     msg.reply_photo(nekos.img(target))



def pussygif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "pussy"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def tits(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "tits"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def holoero(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "holoero"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def pussy(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "pussy_jpg"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def hentaigif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "random_hentai_gif"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def classic(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "classic"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def kuni(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "kuni"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def waifu(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")



def kiss(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "kiss"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def femdom(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "femdom"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def cuddle(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "cuddle"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def erok(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "erok"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def foxgirl(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "fox_girl"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def titsgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "boobs"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def ero(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "ero"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def smug(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "smug"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def baka(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "baka"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))
    

def dva(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    link = nsfw.get("url") 
    link = link[31:],
    if not link:
        message.reply_text("No URL was received from the API!")
        return
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, hexa"),InlineKeyboardButton(text=f"Direct link",url=f"https://dva.computerfreaker.cf/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {message.from_user.id}")]]
    message.reply_photo(f"https://dva.computerfreaker.cf/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))
