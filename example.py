from BurbnBot import Burbnbot

bot = Burbnbot()

# get the following list (take a long time)
users_following = bot.get_following_list()

# get the followers list (take a long time)
users_followers = bot.get_followers_list()

for user in [u for u in users_following if u not in users_followers]:
    # unfollow who don't follow you back
    bot.unfollow(username=user)

# Open hashtag's feed 'creative',
# move to Recent tab and
# click in the first picture
bot.open_tag(tag="creative", tab="Recent")

# swipe and like 5 pictures do feed opened before
bot.like_n_swipe(5)

# open the profile "badgalriri"
bot.open_profile(username="badgalriri", open_post=True)
# swipe and like 3 pictures do feed opened before
bot.like_n_swipe(3)

# open the post https://www.instagram.com/p/B_nrbNPndh0/
bot.open_media(media_code="B_nrbNPndh0")
bot.like_n_swipe()
