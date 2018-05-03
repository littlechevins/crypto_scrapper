#!/usr/bin/env python3

import telegram
from telegram import ParseMode


def main():

    bot = telegram.Bot(token='570371252:AAGwcRvt6anUgyq5Ev9lVzPcHAAkyvD6wYU')

    print(bot.get_me())

    title = "Barely 2 months after one of the worst hacks in crypto history, BitGrail re-opens as if nothing ever happened.\n"

    meta = "*Priority: 3*\n*Comments: 0*\n"

    url = "https://www.reddit.com/r/CryptoCurrency/comments/8ggn9c/barely\_2\_months\_after\_one\_of\_the\_worst\_hacks\_in/"

    tel_send_msg(bot, title, meta, url)

def tel_send_msg(bot, title, meta, url):


    text_msg = (title+'\n'+meta+'\n'+url)

    # text_msg = "Barely 2 months after one of the worst hacks in crypto history, BitGrail re-opens as if nothing ever happened.\n*Priority: 3*\n*Comments: 0*\n"


    bot.send_message(chat_id="@kevscrypto", text=text_msg, parse_mode=telegram.ParseMode.MARKDOWN)


if __name__ == '__main__':
    main()
