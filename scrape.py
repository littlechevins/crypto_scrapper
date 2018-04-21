#!/usr/bin/env python3
# meme
import praw
import pandas as pd
import datetime as dt
from urllib.parse import quote_plus

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print ("Running...")

KEY_WORDS_INC = ['FUD', 'FOMO', 'fud', 'fomo', 'bear', 'bull', 'regulation']
KEY_WORDS_EXC = ['distruption', 'blockfolio', 'checking', 'who']

def main():

    reddit = praw.Reddit(client_id='JSY9BaJfOpWCgQ', \
                         client_secret='ea1yw-Fruyaafav92Y5BCINhNNg', \
                         user_agent='crypto_scrapper', \
                         username='crypto_scrapper', \
                         password='password123')

    # CryptoCurrency+Bitcoin+Btc
    subreddit = reddit.subreddit('CryptoCurrency')

    # flagged = []

    for submission in subreddit.stream.submissions():
        # print("call")
        process_submission(submission)

def process_submission(submission):

    # less than 20 words per title
    if len(submission.title.split()) > 20:
        return

    normalise_title = submission.title.lower()

    url_title = quote_plus(submission.title)
    url_id = (submission.id)
    url_body = (submission.selftext)

    flag = False

    for posts in KEY_WORDS_INC:
        if posts in normalise_title:
            print (color.RED + url_title + color.END)
            # flagged.append(url_id)
            flag = True

    if(flag == False):
        print(url_title)
    else:
        file = open("flagged.txt", "a")
        file.write("==="+url_id+"===================================="+'\n')
        file.write("---"+url_title+"---"'\n')
        file.write(url_body+'\n')
        file.close()



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
