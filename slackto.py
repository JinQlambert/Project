
# coding: utf-8

# In[ ]:


from slacker import Slacker

def send(message):
    
    token = 'xoxb-295111285623-xMQ4NxaJ722POUyyN1DKCGeh'
    slack = Slacker(token)
    slack.chat.post_message('#general', message)

