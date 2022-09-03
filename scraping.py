
# Import Splinter, BeautifulSoup, and Pandas
import numpy  as np
import pandas as pd

import bs4
from   bs4 import BeautifulSoup as soup

import webdriver_manager
from   webdriver_manager.chrome import ChromeDriverManager

import splinter
from   splinter import Browser

import datetime as dt
# This Splinter code will be used in the assignment below.
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser         = Browser(driver_name='chrome',
#                           retry_count=1,
#                           **executable_path,
#                           headless   =True) # set to False if you would like to see the web page

# Selenium 4
#   Selenium 4 code should not be required to run Splinter code.
#   Selenium 4 code is included here for the purposes of explication.
import selenium
from   selenium                          import webdriver
from   selenium.webdriver.chrome.service import Service as ChromeService
from   selenium.webdriver.common.by      import By

from datetime import datetime

import platform
import sys


def scrape_all():
      # Initiate headless driver for deployment
      # Set up Splinter
      executable_path = {'executable_path': ChromeDriverManager().install()}
      browser = Browser('chrome', **executable_path, headless=True)

      news_title, news_paragraph = mars_news(browser)
      img_urls_titles = mars_hemispheres(browser)
      
      # Run all scraping functions and store results in a dictionary
      data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": img_urls_titles,
        "last_modified": dt.datetime.now()
      }

      # Stop webdriver and return data
      browser.quit()
      return data

def mars_news(browser):
      # Scrape Mars News
      # Visit the mars nasa news site
      url = 'https://redplanetscience.com'
      browser.visit(url)

      # Optional delay for loading the page
      browser.is_element_present_by_css('div.list_text', wait_time=1)


      # Convert the browser html to a soup object and then quit the browser
      html = browser.html
      news_soup = soup(html, 'html.parser')
      
      # Add try/except for error handling
      try:
            slide_elem = news_soup.select_one('div.list_text')

            slide_elem.find('div', class_='content_title')


            # Use the parent element to find the first `a` tag and save it as `news_title`
            news_title = slide_elem.find('div', class_='content_title').get_text()
      

            # Use the parent element to find the paragraph text
            news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
      
      except AttributeError:
            return None, None
    
      return news_title, news_p

# ## JPL Space Images Featured Image
def featured_image(browser):

      # Visit URL
      url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
      browser.visit(url)


      # Find and click the full image button
      full_image_elem = browser.find_by_tag('button')[1]
      full_image_elem.click()


      # Parse the resulting html with soup
      html = browser.html
      img_soup = soup(html, 'html.parser')

      try:
            # Find the relative image url
            img_url_rel = img_soup.find('img', class_='headerimage fade-in').get('src')
            
      except AttributeError:
            return None

      # Use the base URL to create an absolute URL
      img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
      img_url

      return img_url


# ## Mars Facts
def mars_facts():
      # Add try/except for error handling
      try:
            # use 'read_html" to scrape the facts table into a dataframe
            df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
            
      except BaseException:
            return None
      
      # Assign columns and set index of dataframe
      df.columns=['Description', 'Mars', 'Earth']
      df.set_index('Description', inplace=True)
      
      # Convert dataframe into HTML format, add bootstrap
      return df.to_html(classes="table table-striped")


def mars_hemispheres(browser):

      # 1. Use browser to visit the URL 
      url = 'https://marshemispheres.com/'
      browser.visit(url)

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
      return hemisphere_image_urls


if __name__ == "__main__":

      # If running as script, print scraped data
      print(scrape_all())

