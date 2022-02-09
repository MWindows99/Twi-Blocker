import tweepy

# API Key
API_KEY = 'xxxx'
API_SECRET = 'xxxx'
ACCESS_TOKEN = 'xxxx-xxxx'
ACCESS_TOKEN_SECRET = 'xxxx'
# ブロック対象の用語
words = "裏アカ女子"

# Create Object
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print("Collecting follower information...")
follower = tweepy.Cursor(api.get_follower_ids, cursor = -1).items()
follower_list = []

for followers in follower:
    follower_list.append(follower)

print("Checking follower description...")
while len(follower_list) > 0:
    user_check = follower_list.pop(0)
    description = str(api.get_user(user_id=user_check).description)
    if words in description:
        #block
        api.create_block(user_id=user_check)
        print("Twitter User has been blocked! UserID:" + str(user_check))
    else:
        pass
print("Complete!!")
