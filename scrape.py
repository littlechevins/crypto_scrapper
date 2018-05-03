#!/usr/bin/env python3
# meme
import praw
import pandas as pd
import datetime as dt
from urllib.parse import quote_plus
import re

import telegram
from telegram import ParseMode
from telegram_bot import tel_send_msg



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[34m'
   GREEN = '\033[32m'
   YELLOW = '\033[33m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print ("Searching...")

# KEY_WORDS_INC = ['FUD', 'FOMO', 'fud', 'fomo', 'bear', 'bull', 'regulation']
# KEY_WORDS_EXC = ['distruption', 'blockfolio', 'checking', 'who', 'skyrocket']

telegram_bot = telegram.Bot(token='570371252:AAGwcRvt6anUgyq5Ev9lVzPcHAAkyvD6wYU')


def main():

    scan_all_submissions()
    # url_sanitiser("https://www.reddit.com/r/CryptoCurrency/comments/87z9ye/ignore_the_conspiracies_this_is_why_crypto_crashed/")

def scan_all_submissions():
    reddit = praw.Reddit(client_id='JSY9BaJfOpWCgQ', \
                         client_secret='ea1yw-Fruyaafav92Y5BCINhNNg', \
                         user_agent='crypto_scrapper', \
                         username='crypto_scrapper', \
                         password='password123')

    # CryptoCurrency+Bitcoin+Btc
    subreddit = reddit.subreddit('CryptoCurrency')

    include = []
    file2list(include, "include.txt")
    print(include)

    for submission in subreddit.stream.submissions():
        process_submission(submission, include)

def process_submission(submission, include):

    # less than 20 words per title
    if len(submission.title.split()) > 20:
        return

    normalise_title = submission.title.lower()

    url_title = (submission.title)
    url_id = (submission.id)
    url_body = (submission.selftext)
    url_url = (submission.url)
    url_num_comm = (submission.num_comments)

    flag = False
    priority = 0

    for posts in include:
        if posts in normalise_title:
            flag = True
            priority+=1


    # if(flag == False):
    #     print(url_title)
    # else:
    #     file = open("flagged.txt", "a")
    #     file.write("==="+url_id+"===================================="+'\n')
    #     file.write("---"+url_title+"---"'\n')
    #     file.write(url_body+'\n')
    #     file.close()


    metadata = ("Priority: *" + str(priority) + "*\nComments: *" + str(url_num_comm) + "*\n")

    if priority > 3:
        print (color.RED + url_title + color.END)
        python2telegram(url_title, metadata, url_url)
    elif priority == 2:
        print (color.YELLOW + url_title + color.END)
        python2telegram(url_title, metadata, url_url)
    elif priority == 1:
        print (color.BLUE + url_title + color.END)
    else: # priority = 0
        print(url_title)


    priority = 0 #saftey lol


def url_sanitiser(url):
    output = re.sub("_", "\_", url)
    print(output)
    return output

def file2list(include, filename):
    f = open(filename, "r")
    for line in f:
        if not(re.search('^\#.*', line)):
            include.append(line.strip())
    f.close()
    # removes empty string cause...bug in above
    include = list(filter(None, include))

def python2telegram(url_title, metadata, url_url):
    tel_send_msg(telegram_bot, url_title, metadata, url_sanitiser(url_url))

# top_subreddit = subreddit.top(limit=5)
#
# topics_dict = {"title":[], \
#                "score":[], \
#                "id":[], "url":[], \
#                "comms_num":[], \
#                "created":[], \
#                "body":[]}
#
# for post in top_subreddit:
#     topics_dict["title"].append(post.title)
#     topics_dict["score"].append(post.score)
#     topics_dict["id"].append(post.id)
#     topics_dict["url"].append(post.url)
#     topics_dict["comms_num"].append(post.num_comments)
#     topics_dict["created"].append(post.created)
#     topics_dict["body"].append(post.selftext)
#
#
# def get_date(created):
#     return dt.datetime.fromtimestamp(created)
#
# topics_data = pd.DataFrame(topics_dict)
#
# _timestamp = topics_data["created"].apply(get_date)
#
# topics_data = topics_data.assign(timestamp = _timestamp)

# # print(topics_data)
# for titles in topics_data:
#     print (titles.title)

# print ("Killing...")
if __name__ == '__main__':
    main()
