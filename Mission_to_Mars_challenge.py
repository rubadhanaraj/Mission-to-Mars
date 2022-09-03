#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy  as np
import pandas as pd

import bs4
from   bs4 import BeautifulSoup as soup

import webdriver_manager
from   webdriver_manager.chrome import ChromeDriverManager

import splinter
from   splinter import Browser

import selenium
from   selenium                          import webdriver
from   selenium.webdriver.chrome.service import Service as ChromeService
from   selenium.webdriver.common.by      import By

from datetime import datetime
import platform
import sys


# In[41]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[42]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[43]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[44]:


slide_elem.find('div', class_='content_title')


# In[45]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[46]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[47]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[48]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[49]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[50]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='headerimage fade-in').get('src')
img_url_rel


# In[51]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[52]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[53]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 

# ### Hemispheres

# In[54]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[55]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
    
for i in range(4):
    # Browse through each link to get all the titles and images
    browser.links.find_by_partial_text('Hemisphere')[i].click()
    
    # Parse the HTML
    html = browser.html
    hemisphere_soup = soup(html,'html.parser')
    
    # Scraping
    title = hemisphere_soup.find('h2', class_='title').text
    img_url = hemisphere_soup.find('li').a.get('href')
    
    # Create a dictionary and store the images and titles using append function  
    hemispheres = {}
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()


# In[56]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[57]:


# 5. Quit the browser
browser.quit()

