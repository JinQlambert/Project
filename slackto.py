
# coding: utf-8

# In[ ]:


def send(today_attendance):
    
    token = 'xoxb-295111285623-xMQ4NxaJ722POUyyN1DKCGeh'
    slack = Slacker(token)
    slack.chat.post_message('#general', today_attendance)

