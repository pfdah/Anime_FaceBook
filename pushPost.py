#Modules
from keys import page_access_token,fb_page_id
import facebook
import schedule
import time
import random

#Stuffs that help in verification
graph = facebook.GraphAPI(page_access_token)

# five_post = ["This is random post","IDK in what order will this be posted.","God I hope this is first.","Be the last one.","God bless Anime."]
# def job():
#     message = five_post.pop(random.randint(0,len(five_post)))
#     print("Posting started")
#     graph.put_object(fb_page_id, "feed", message=message)
#     print("Posting completed")

print("Post started")
message = "This is initial testing of automatic facebook posts using python.\nNow I will do some other testings, and later implement the Anime API and create 2 hourly posts about anime."
graph.put_object(fb_page_id, "feed", message=message)
print("Post ended")

# schedule.every(180).seconds.do(job)
# while True:
#   schedule.run_pending()
#   time.sleep(1)
  
