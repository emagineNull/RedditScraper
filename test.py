import webbrowser

import numpy as np
from sklearn.datasets import load_iris
import praw
from praw.models import MoreComments
import pandas as pd

reddit_authorized = praw.Reddit(client_id="PnMLfwXko3nXvtYnNULf2A",
                               client_secret="fMQtNuWSHYJlsUVbg3De7z6F5cJPew",
                               user_agent="Scraping",
                                username="emagine9",
                                password="pichasreddit3")

subreddit = reddit_authorized.subreddit("Python")


print("Display Name:", subreddit.display_name)
print("Title:", subreddit.title)
print("Description:", subreddit.description)


for post in subreddit.hot(limit=5):
    print(post.title)
    print()

posts = subreddit.top(time_filter="month", limit=5)

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Post Text"].append(post.selftext)
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)


top_posts = pd.DataFrame(posts_dict)
print(top_posts.to_string())

url = "https://www.reddit.com/r/Python/comments/iehths/debugging_cheat_sheet/"
    
submissions = reddit_authorized.submission(url=url)

post_comments = []

for comment in submissions.comments:
    if type(comment) == MoreComments:
        continue

    post_comments.append(comment.body)


comments_df = pd.DataFrame(post_comments, columns=['comments'])
print(comments_df.to_string())

