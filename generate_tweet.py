import tweepy
from config import authenticate

def get_trending_topic():
    client = authenticate()
    
    # Get trending topics for a specific location (WOEID 1 = Worldwide)
    trends = client.get_place_trends(id=1)
    
    if trends and "trends" in trends.data:
        top_trend = trends.data["trends"][0]["name"]
        return top_trend
    return "No trends found."

def generate_tweet():
    trend = get_trending_topic()
    tweet_text = f"Today's trending topic: {trend}. What are your thoughts? #TrendingNow"
    return tweet_text
