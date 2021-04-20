import tweepy
import time

auth = tweepy.OAuthHandler('GU91gQbpKANigrmzvNLzu83sU', 'h9rGCUoqMeC6pUVOr1nT9PEwnNN9Kc2GWQZsGsCOj0VR400VK')   #n
auth.set_access_token('3285277854-m2ey7AKBNPp7Ri4B8AspaeUxPs6DCKHZJzLWTIE', 'FCHSeGKfO9ROQoGr34ww4CMJITzMTgKgi1K23c7FcULz') #d

api = tweepy.API(auth)
user = api.me()

# bot for following people

def limit_handeler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

for follower in limit_handeler(tweepy.Cursor(api.followers).items()):
    follower.follow()
    print(f'you followed : {follower.name}')
