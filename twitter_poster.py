import tweepy


def post_tweet(api_key, api_secret, access_token, access_token_secret, message):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)


# 使用示例
api_key = "your_api_key"
api_secret = "your_api_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
message = "Hello, Twitter!"
post_tweet(api_key, api_secret, access_token, access_token_secret, message)
