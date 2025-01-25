import tweepy

# Replace with your credentials
consumer_key = 'IbhYXOvHdvNAtY0Oj6HpamhPa'           # Replace with your actual consumer key
consumer_secret = 'cDGKt6n1VBIVG8hXxlktc5u5DQmXgkzg9N01llyiSB0EyXpivT'     # Replace with your actual consumer secret
access_token = '1848432529860399110-QWCybm7fH4Vz6pxQa3szVUpYF5s8rW'           # Replace with your actual access token
access_token_secret = 'OmojY7a552zXhnjrSJfzvP37LTFxqKusDWVskvL6Ookg8'  # Replace with your actual access token secret

# Authenticate with Twitter/X API
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# ✅ Example: Post a Tweet
response = client.create_tweet(text="Hi again, X! #TwitterBot")
print(f"Tweet posted! ID: {response.data['id']}")
