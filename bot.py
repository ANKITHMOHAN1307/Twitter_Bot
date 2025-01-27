import schedule
import time
from config import authenticate
from generate_tweet import generate_tweet

# Initializing Twitter client
client = authenticate()

def tweet_trending_topic():
    tweet_text = generate_tweet()
    client.create_tweet(text=tweet_text)
    print("Tweet posted:", tweet_text)

# Schedule to run at the given time
schedule.every().day.at("00:00").do(tweet_trending_topic)

print("Twitter bot started... Tweets will be posted at midnight.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for the next minute before checking again
