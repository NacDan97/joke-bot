import praw
import json
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
