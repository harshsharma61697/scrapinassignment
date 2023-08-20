#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install request')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


import pandas as pd


# In[4]:


import re


# # Question1:("https://en.wikipedia.org/")

# In[9]:


page0=requests.get("https://en.wikipedia.org/")


# In[10]:


page0


# In[11]:


soup4=BeautifulSoup(page0.content)
soup4


# In[12]:


H1=soup4.find("span",class_="mw-headline")
H1.text


# In[13]:


list1=[]
for i in soup4.find_all("span",class_="mw-headline"):
    list1.append(i.text)
list1


# In[16]:


import pandas as pd


# In[17]:


import pandas as pd


# In[26]:


DF=pd.DataFrame(list1,columns=["All_header"])


# In[27]:


DF


# # Question2:https://www.cnbc.com/

# In[28]:


page=requests.get("https://www.cnbc.com/")


# In[29]:


page


# In[30]:


soup3=BeautifulSoup(page.content)


# In[31]:


soup3


# In[32]:


time=soup3.find( "time" ,  class_="LatestNews-timestamp")
time.text


# In[33]:


Time=[]
for i in soup3.find_all(   "time",class_="LatestNews-timestamp"):
    Time.append(i.text)
    
Time


# In[34]:


len(Time)


# In[35]:


headline=[]

for i in soup3.find_all("a",class_="LatestNews-headline"):
    headline.append(i.text)
headline


# In[37]:


len(headline)


# In[38]:


df=pd.DataFrame[{"Head_line":headline,"Newes_Time":Time}]


# In[42]:


df=pd.DataFrame(list(zip(headline,Time)),columns=["Head_line","Update_time"])


# In[43]:


df


# # Question3:https://www.journals.elsevier.com/artificial¶

# In[44]:


page=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")


# In[45]:


page


# In[46]:


soup2=BeautifulSoup(page.content)
soup2


# In[48]:


Paper=[]
for i in soup2.find_all( "h2",class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg" ):
    Paper.append(i.text)
    
Paper


# In[49]:


Aother_name=[]
for i in soup2.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Aother_name.append(i.text)
Aother_name


# In[50]:


P_date=[]
for i in soup2.find_all("span",class_="sc-1thf9ly-2 dvggWt"):
    P_date.append(i.text)
    
P_date


# In[ ]:


df=pd.DataFrame(list(zip(headline,Time)),columns=["Head_line","Update_time"])


# In[52]:


Dataframe=pd.DataFrame(list(zip(Paper,Aother_name,P_date)),columns=["Artical","Aother_Name","Publish_Date"])


# In[53]:


Dataframe


# # Question4'https://www.dineout.co.in/delhi-restaurants/buffet-special')

# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[9]:


page


# In[10]:


soup=BeautifulSoup(page.content)
soup


# In[11]:


restaurant_name=[]

for i in soup.find_all("a",class_="restnt-name ellipsis"):
     restaurant_name.append(i.text)
    
restaurant_name    


# In[12]:


loc=[]

for i in soup.find_all("div" ,   class_= "restnt-loc ellipsis"):
    loc.append(i.text)
    
loc


# In[13]:


image=[]

for i in soup.find_all("img",class_="no-img"):
    
    image.append(i.get('data-src'))
image    


# In[14]:


gh=[]
for i in soup.find_all("span",class_="double-line-ellipsis"):
    gh.append(i.text)
gh


# In[17]:


rating=[]
for i in soup.find_all("div",class_="restnt-rating-widget pull-right text-right"):
    rating.append(i.text)
    
rating


# In[18]:


DFO=pd.DataFrame(list(zip(restaurant_name,loc,image,gh,rating)),columns=["Restaurnt_Name","Location","Image","Rate_Cuisine","Rating"])


# In[19]:


DFO


# # Question5:icc-cricket.com

# In[5]:


page= requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[6]:


page_html=page.text
soup8=BeautifulSoup(page_html,"html.parser")
soup8


# In[7]:


player=[]
for tr in soup8:
    for td in soup8:
        player.append(td.text.replace("\n"," ").strip())
        

print(player)  


# In[ ]:




