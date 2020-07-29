#imports
from instapy import InstaPy
from instapy import smart_run
import random
import os
from os import path
from pathlib import Path

# login credentials
insta_username = 'username'
insta_password = 'password'

#check for and delete old cookie
home = str(Path.home())

if path.exists(home + "/InstaPy/logs/" + insta_username + "/" + insta_username + "_cookie.pkl"):
  print("Deleting Existing Cookie")
  os.remove(home + "/InstaPy/logs/" + insta_username + "/" + insta_username + "_cookie.pkl")

#array of hashtags to like and the min and max range for number of likes
hashtags_to_like = ["hashtag1","hashtag2"]
min_likes = 5
max_likes = 20

# get an InstaPy session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  # general settings		

  # activity		
    for x in hashtags_to_like:
    print(session.like_by_tags([x], amount=random.randrange(min_likes,max_likes)))

