#create a reddit bot that posts a random quote from the main page of reddit
from ast import Break
import praw
import random
import time
import os
import json
import urllib.request
import re
import requests
import configparser
import concurrent.futures
import argparse


def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = "HappyCollectBot",
                    password = "",
                    client_id = "pi5kqmgWrr538iIuq7ooNw",
                    client_secret = "VT0gKsALyr3P7fqS6Qx5Z8OUAaj8gQ",
                    user_agent = "HappyCollectBot v0.1")
    print("Logged in!")
    return r

enterSub = input("Enter the subreddit you want to collect from: ").lower()
enterLim = input("Enter the number of submissions you want to collect: ")


def bot_post(r):
    print("Collecting quotes...")
    subreddit = r.subreddit(enterSub)
    hot_quotes = subreddit.hot(limit=int(enterLim))
    for submission in hot_quotes:
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")

    print("Quotes collected!")

    print("Posting to Reddit...")

    for submission in hot_quotes:
        submission.reply("Title: " + submission.title + "\n" + "Text: " + submission.selftext + "\n" + "Score: " + str(submission.score))
        print("Posted!")

    
    




def save_submissions(submissions):
#create folder for each subreddit
    if not os.path.exists(enterSub):
        os.makedirs(enterSub)
        #create file for each subreddit
        with open(enterSub + "/" + enterSub + ".txt", "a") as f:
            for submission in submissions:
                if submission.id not in open(enterSub + "/" + enterSub + ".txt").read():
                    f.write(submission.id + "\n")
                    f.write(submission.title + "\n")
                    f.write(submission.selftext + "\n")
                    f.write(str(submission.score) + "\n")
                    f.write("---------------------------------\n")





#Function that creates a file for the submissions and saves the data
#check if file has duplicates
#if not, save to file
def save_submissions(submissions):
    with open(enterSub+".txt", "a") as f:
        for submission in submissions:
            if submission.id not in open(enterSub+".txt").read():
                f.write(submission.id + "\n")
                f.write(submission.title + "\n")
                f.write(submission.selftext + "\n")
                f.write(str(submission.score) + "\n")
                f.write("---------------------------------\n")
    
    






def main():
    r = bot_login()
    while True:
        bot_post(r)
        save_submissions(r.subreddit(enterSub).hot(limit=int(enterLim)))#save the submissions to a file
        time.sleep(10)



if __name__ == "__main__": 
    main()

