Twitter Bot using Python and X API

Overview

This Twitter bot is built using Python and the Tweepy library to automate interactions on X (formerly Twitter). It can perform tasks such as posting tweets, liking tweets, retweeting, and responding to specific keywords. The bot uses OAuth authentication to securely access the X API.

Features

Auto-tweet at scheduled intervals

Like and retweet based on specific keywords

Respond to mentions automatically

Fetch trending hashtags

Follows back users who follow the bot

Requirements

Python 3.x

Twitter Developer Account

Tweepy library

Setup Instructions

Create a Twitter Developer Account

Go to developer.twitter.com and create an app.

Generate API keys and access tokens (Consumer Key, Consumer Secret, Access Token, Access Secret).

Install Dependencies

pip install tweepy schedule

Configure API Keys

Create a .env file and store the keys securely:

CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_TOKEN=your_access_token
ACCESS_SECRET=your_access_secret

Run the Bot

python bot.py

Usage

Modify bot.py to define custom behaviors like auto-replies, following users, and fetching trending topics.

Use schedule to automate tweets at fixed intervals.

Deployment

Deploy on cloud platforms like Heroku or AWS for continuous execution.

Use cron jobs or scheduled tasks to automate execution.

Contributing

Feel free to fork this repository, improve the bot, and submit pull requests.
