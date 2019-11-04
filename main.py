import time
from sites import (beebom, digit)

# initiate all sites
beebom = beebom.Beebom()
digit = digit.Digit()

# get all posts from all sites
beebom_post = beebom.latest_post()
digit_post = digit.latest_news()


while True:
    # Beebom
    curr_time = int(time.time())
    new_post_beebom = beebom.latest_post()
    if new_post_beebom['time'] > beebom_post['time']:
        print('Found new post on Beebom!', new_post_beebom)
        beebom_post = new_post_beebom
    else:
        print('No new post found on beebom')

    # Digit
    curr_title = digit_post['title']
    new_post_digit = digit.latest_news()
    if curr_title != new_post_digit['title']:
        print('New Post found on digit!', new_post_digit)
        digit_post = new_post_digit
    else:
        print('No new post found on digit')

    
    
    time.sleep(60)
    
