#!/usr/bin/env python
# coding: utf-8

# In[18]:


import nltk
import numpy as np
import pandas as pd
from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize
import re


# In[14]:


url = 'https://www.bbc.com/urdu/sport-49174685'
html = request.urlopen(url).read().decode('utf8')


# In[55]:


raw = BeautifulSoup(html, 'html.parser').get_text()
raw = raw.translate ({ord(c): " " for c in "\\!@#$%^&*\'\"()[]{};:,./<>?\|`~-=_+\n"})
tokens = word_tokenize(raw)
tokens = [w for w in tokens if not re.match(r'[A-Z]+', w, re.I)]
tokens = [w for w in tokens if not re.match(r'[0-9]+', w, re.I)]
len(tokens)


# In[ ]:




