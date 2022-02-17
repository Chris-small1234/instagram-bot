from instapy import InstaPy


insta_username = 'westiedesign'
insta_password = 'westie4123'

like_tag_list = ['python', 'javascript']


session = InstaPy(username=insta_username,
                  password=insta_password,)

# session.login()
                  
session.like_by_tags(tags=like_tag_list, amount=3)

session.end()