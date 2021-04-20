import tweepy
import time

auth = tweepy.OAuthHandler('GU91gQbpKANigrmzvNLzu83sU', 'h9rGCUoqMeC6pUVOr1nT9PEwnNN9Kc2GWQZsGsCOj0VR400VKn')
auth.set_access_token('3285277854-m2ey7AKBNPp7Ri4B8AspaeUxPs6DCKHZJzLWTIE', 'FCHSeGKfO9ROQoGr34ww4CMJITzMTgKgi1K23c7FcULzd')

api = tweepy.API(auth)
user = api.me()

# bot for like tweets

def limit_handeler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        print('RateLimitError')
        time.sleep(1000)

string = 'covid-19'

for tweet in limit_handeler(tweepy.Cursor(api.search, string).items(10)):
    try:
        tweet.favorite()
        print('I like it')
    except tweepy.error.TweepError as e:
        print(e.reason)