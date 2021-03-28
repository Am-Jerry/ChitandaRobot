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


from telegram import Update

from telegram.ext import CallbackContext

def asfile(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    query = update.callback_query
    message = query.message
    data = query.data.split(", ")
    query_type = data[0]
    user_id = data[1]
   
    if query_type == "neko_callback":
        if data[2] == 'hexa':
            data = data[1][2:]
            data = data[:-3]
            link = f"https://dva.computerfreaker.cf/{data}"
            message.reply_document(link)
            
        elif data[2] == 'neko':
            data = data[1][2:]
            data = data[:-3]
            link = f"https://cdn.nekos.life/{data}"
            message.reply_document(link)
            
    elif query_type == "neko_delete":
        if query.from_user.id == int(user_id):
            bot.answer_callback_query(query.id,
                                      text="Deleted!"
                                      )
            message.delete()
        else:
            bot.answer_callback_query(query.id,
                                      text="You're not allowed to use this."
                                      )
       
