#!/usr/bin/env python
# coding: utf-8

# # Requests Introduction

# ### rquests.get(url): 可以擷取網站資料。

# ### requests擷取的資料格式為Response。

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import requests, bs4


# In[4]:


url="https://walkbell-awards.com/Home/Shortlisted"
htmlfile=requests.get(url)
print(type(htmlfile))


# In[5]:


print('是否成功獲取網路內容',htmlfile.status_code) #列印出200表示成功獲取。
print('列印出網頁內容\n', htmlfile.text) #\n表示換行。


# ### 搜尋網頁特定內容

# In[6]:


import requests


# In[7]:


import re


# In[8]:


url="https://walkbell-awards.com/Home/Shortlisted"
htmlfile=requests.get(url)

word=input("請輸入想搜尋的字串：")

if word in htmlfile.text:
    print("搜尋成功")
    data=re.findall(word,htmlfile.text) #將搜尋到的字放入串列中。ex.[1,2,3,4,5]
    print("出現次數：",len(data))

else:
    print("搜尋失敗")


# ### 確認程式是否有成功抓取資料

# In[9]:


import requests


# In[10]:


url="https://walkbell-awards.com/Home/Shortlisted"
htmlfile=requests.get(url)

if htmlfile.status_code == 200:
    print("列印出網頁內容:\n",htmlfile.text)
else:
    print("網頁下載失敗")
    print(htmlfile.raise_for_status())


# ### 使用raise_for_status() 找出錯誤原因。

# ### 400 Client Error: 代表金石堂需要存取權限才可以下載資料。

# ### 新增表頭並偽裝成瀏覽器。

# ### 放入headers之後，金石堂的資料就可以讀取囉！

# In[11]:


import requests
url="https://www.kingstone.com.tw/"
headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
htmlfile=requests.get(url,headers=headers)

if htmlfile.status_code == 200:
    print("列印出網頁內容\n", htmlfile.text)
    
else:
    print("網頁下載失敗")
    print("失敗原因\n",htmlfile.raise_for_status())


# ### time.sleep ：每次抓取的時候停頓幾秒，避免網站察覺連續性不正常的爬蟲程式。

# ### random.randint(min, max): 每次執行會出現min-max之間的任意整數。

# In[12]:


import requests


# In[13]:


import time


# In[14]:


import random


# In[15]:


url="https://walkbell-awards.com/Home/Shortlisted"
headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}

for i in range(3): #程式執行三次
    htmlfile=requests.get(url,headers=headers)
    if htmlfile.status_code == 200:
        print("列印出網頁內容:\n",htmlfile.text)
    else:
        print("網頁下載失敗")
        print(htmlfile.raise_for_status())
    time.sleep(random.randint(1,5)) #程式每次會停頓1-5秒。


# # urllib Introduction

# ### urlopen(url): 可以擷取網站資料。

# ### urllib.request擷取的格式為HTTPResponse。

# In[16]:


import urllib.request

url="https://www.python-graph-gallery.com/violin-plot/"
htmlfile=urllib.request.urlopen(url)
print(type(htmlfile))


# ### read()：可以顯示urlopen擷取後的資料。

# ### decode('utf-8'): 可以顯示中文。

# In[17]:


import urllib.request

url="https://www.ntu.edu.tw/"
htmlfile=urllib.request.urlopen(url)
print(htmlfile.read().decode('utf-8'))


# ### HTTPResponse物件常用屬性

# ### geturl(): 取的網站連結。
# ### status: 網站擷取成功會顯示200。
# ### getheaders(): 取得表頭內容。

# In[18]:


import urllib.request

url="https://www.ntu.edu.tw/"
htmlfile=urllib.request.urlopen(url)
print("物件網址：", htmlfile.geturl())
print("下載情形：", htmlfile.status)
print("表頭內容：", htmlfile.getheaders())


# ### 如果存取被阻擋，需要輸入Request建立headers

# In[19]:


import urllib.request

url="https://smiletaiwan.cw.com.tw/"
headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}

req=urllib.request.Request(url,headers=headers)
htmlfile=urllib.request.urlopen(req)
print(htmlfile.read().decode('utf-8'))


# # BeautifulSoup Introduction

# ### 確認BeautifulSoup的資料型態為bs4.BeautifulSoup

# In[20]:


import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)

soup=bs4.BeautifulSoup(htmlfile.text,'lxml')
print(type(soup))


# In[21]:


import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)

soup=bs4.BeautifulSoup(htmlfile.text,'lxml')
print("物件類型:",type(soup.title))
print("title標籤:", soup.title)
print("title標籤內容:",soup.title.text)


# ### find(): 尋找文件標籤內第一個符合的內容。

# In[22]:


import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag=soup.find('h2')

print("物件類型:",type(objtag))
print("列印標籤:", objtag)
print("列印標籤內容:", objtag.text)


# ### find_all(): 尋找所有符合文件標籤的內容。

# In[23]:


import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag=soup.find_all('h2')

print("物件類型:",type(objtag))
print("列印標籤:", objtag)


# ### 每一個h2的資料型態為bs4.element.Tag

# In[24]:


print(type(objtag[0]))


# In[25]:


print("方法一：")
for data in objtag:
    print(data.text)


# In[26]:


print("方法二：")
for data in objtag:
    print(data.getText())


# In[27]:


print("方法三：")
for data in objtag:
    print(str(data))


# In[28]:


print("方法四：")
for i in range(len(objtag)):
    print(objtag[i])


# ### 使用html標籤屬性搜尋

# ### id='title','content'

# In[29]:


import bs4

import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_1=soup.find(id="content")
print("物件類型:",type(objtag_1))
print("列印標籤:", objtag_1)
print("列印標籤內容:", objtag_1.text)


# ### class_="section"

# In[30]:


import bs4

import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_1=soup.find(class_="site-header")
print("物件類型:",type(objtag_1))
print("列印標籤:", objtag_1)
print("列印標籤內容:", objtag_1.text)


# In[31]:


for data in objtag_1:
    print(data.text)


# ### select() 跟find_all() 一樣，會找到所有對應屬性的資料。

# In[32]:


import bs4

import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_2=soup.select("h2")
print("物件類型:",type(objtag_2))
print("列印標籤:", objtag_2)


# In[33]:


for data in objtag_2:
    print(data.text)


# ### 使用select(): 如果開頭是class_= 則用.表示。

# In[34]:


import bs4

import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_2=soup.select(".entry-content")
print("物件類型:",type(objtag_2))
print("列印標籤:", objtag_2)


# ### 使用select(): 如果開頭是id= 則用#表示。

# In[35]:


import bs4

import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_2=soup.select("#post-2465")
print("物件類型:",type(objtag_2))
print("列印標籤:", objtag_2)


# ### 取得圖片網址

# ### find('img')

# In[36]:


import bs4

import requests,bs4

url="https://kimshieh.com/"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

img=soup.find('img')
print("圖片網址:", img['src'])


# ### 以維基百科為例

# ### h1標題

# In[37]:


import bs4

import requests,bs4

url="https://zh.m.wikipedia.org/zh-tw/%E7%AC%AC4%E5%B1%86%E8%B5%B0%E9%90%98%E7%8D%8E"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag=soup.find('h1')
print(objtag.text)


# ### 小標題 class_="toctext"

# In[38]:


import bs4

import requests,bs4

url="https://zh.m.wikipedia.org/zh-tw/%E7%AC%AC4%E5%B1%86%E8%B5%B0%E9%90%98%E7%8D%8E"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_2=soup.find_all(class_="toctext")

for item in objtag_2:
    print(item.text)


# ### 找出表格 td

# In[39]:


import bs4

import requests,bs4

url="https://zh.m.wikipedia.org/zh-tw/%E7%AC%AC4%E5%B1%86%E8%B5%B0%E9%90%98%E7%8D%8E"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_4=soup.find_all("td")

for item in objtag_4:
    print(item.text)


# In[40]:


import bs4

import requests,bs4

url="https://zh.m.wikipedia.org/zh-tw/%E7%AC%AC4%E5%B1%86%E8%B5%B0%E9%90%98%E7%8D%8E"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

objtag_4=soup.find_all("tr")

for item in objtag_4:
    print(item.text)


# ### 爬取表格2.0

# In[41]:


import bs4

import requests,bs4

url="https://zh.m.wikipedia.org/zh-tw/%E7%AC%AC4%E5%B1%86%E8%B5%B0%E9%90%98%E7%8D%8E"
htmlfile=requests.get(url)
soup=bs4.BeautifulSoup(htmlfile.text,'lxml')

tableobj=soup.find_all("tr")
print(tableobj)

print('-'*100)

classification=[] 

for data in tableobj[17:]:
    content=data.find_all('td')
    print(content)
    classification.append(content[0].text)
    
print("-"*100)

print(classification)

# print(name)

# print("-"*100)
# table=dict(zip(classification, name))
# print(table)
    

