from instapy import InstaPy

# session = InstaPy(username="westiedesign", password="westie4123#")
# session.login()

"""
This template is written by @timgrossmann

What does this quickstart script aim to do?
- This script is automatically executed every 6h on my server via cron
"""

import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'westiedesign'
insta_password = 'westie4123'


friends = ['list of friends I do not want to interact with']

like_tag_list = ['python', 'javascript']

ignore_list = ['.net', 'c#']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)

    session.set_dont_include(friends)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)


session.end()