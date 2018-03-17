import praw
import json
import schedule
import time
import random
import disc_run
from redcreds import *

data = {'jokes' : []}

def main():
    reddit = praw.Reddit(client_id = client_id,
                         client_secret = client_secret,
                         user_agent = user_agent,
                         username = username,
                         password = password)

    for submission in reddit.subreddit('jokes').top(limit = 10000):

        if submission.score >= 2500:
            data['jokes'].append({
                'r/jokes' : {
                'title' : submission.title,
                'text' : submission.selftext,
                'link' : submission.url,
                }
            })

            with open("redditJokes.json", "w+") as f:
                json.dump(data,f, indent = 4, sort_keys = False)

main()

'''
Setting up a schedule for the main function
to be called causes an issue of starting the bot.

schedule.every().day.at("12:00").do(main)
time.sleep(10)

while True:
 schedule.run_pending()
 time.sleep(1)
'''
