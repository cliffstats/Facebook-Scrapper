

# coding: utf-8
# # FACEBOOK SCRAPER
#import all dependecies
import facebook as fb
import _pickle
import random
import requests
import json, csv
import pandas as pd
import math

## Set up token and required variables

token = "EAAWcTS6f2msBAFhFwUhYaEsA69bY6T5cUVt8JjyEMWrXapjluckcAsX1je7M7zOZCfBRKH30cthSzhjQEEC3HFotFMrD0mnSURLhER8VZBWOke2x8zyWLfrnIakJQ8PlrmgTPeZCnL7BZBviagHyQZCKRCPRnbUyEdZCjJa3kKQAZDZD"
## system to read input from other source(ie csv,txt,pkl file)
user_id='2165316316832044'
page_id='giggsinvetstment'
keyword='Using'

#load access token
graph = fb.GraphAPI(token)
#system to directly take input
#user_id = input("Insert unique User_id here: ")
#keyword = input("Insert keyword here: ")
#page = input("Insert unique page name here: ")
#print(user_id, keyword, page)
# ##  Srape data using User_id
# In[232]:
# Get Users posts
fb_data = graph.get_object(user_id+'?fields=id,name,posts,likes,friends')
fb_data.keys()
# ## Check if data is scrapped incorrect format

# In[233]:
if type(fb_data)==dict:
    print('Conratulations! The Posts scraping was successfull')
elif type(fb_data)!=dict:
    print('Sorry! We couldn\'t complete your request')
# ## Check the User's total number of friends
# In[234]:
friends=fb_data['friends']['summary']['total_count']
print('The User\'s total number of friends are', friends)
# ## Structure the posts into a data frame
# In[355]:
post=fb_data['posts']['data']
post_data = pd.DataFrame(post)
post_data.head(5)
post_data.keys()
#post_data['message']
# ## Check if User's posts contain keyword
# In[346]:
posts=post_data['message']
posts_bin= posts.str.contains(keyword, regex=False)
if True in posts_bin:
    print('User has posts with keyword "',keyword.upper(),'"')
elif True not in posts_bin:
    print('User has no posts with keyword',keyword.upper(),'"' )


# ## Print out Posts with keyword

# In[353]:


rs=posts_bin.index[posts_bin==True]
post_keyword=pd.DataFrame(posts[rs])
post_keyword=post_keyword.replace('\n','  ',regex=True)
post_keyword


# ## Check Likes data and re-structure it

# In[360]:


likes=fb_data['likes']['data']
likes_data = pd.DataFrame(likes)
likes_data.head(5)


# In[427]:


pages_liked = likes_data['name']
pages_liked.head(5)


# ## Scrape posts using page name

# In[567]:


pages_post = graph.get_object(page_id+'?fields=id,name,fan_count,new_like_count,location,posts{comments,reactions}')
if type(pages_post)==dict:
    print('Conratulations! The Page was scraping successfull')
#me?fields=id,name,posts{comments,reactions},fan_count,new_like_count,location


# ## Structure the page results into a dataframe

# In[568]:


#check name of page scrapped
print('the Page Name is',pages_post['name'])
print('the Page ID name is',pages_post['id'])
print('the Page Followers is',pages_post['fan_count'])
print('the Physical Location is',pages_post['location'])
pages_post.keys()


# ## Scrap data using page unique name

# In[638]:


pages_posts = graph.get_object(page_id+'?fields=posts')
pages_posts.keys()

k=pages_posts['posts']['data']
type(k)
w=[0,1,2,3,4,5,6,7,8]
for i in w:
    if 'message' in k[i]:
        print(k[i]['message'])


#print(type(d))


# In[658]:
keyword2='data'
d=[0,1,2,3,4,5]
for i in d:
    if keyword2 in k[i]['message']:
        print('POSTS WITH KEYWORD FOUND!')
        print(k[i]['id'])
        print(k[i]['message'])
    elif keyword2 not in k[i]['message']:
        print('POSTS WITH KEYWORD NOT FOUND!')

