
# coding: utf-8

# In[ ]:


from slacker import Slacker



def send(token, message):
    slack = Slacker(token)
    slack.chat.post_message('#general', message)
    
    

