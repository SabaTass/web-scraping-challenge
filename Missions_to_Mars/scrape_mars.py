# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import time

# Define scrape function
def scrape():
    # Create a library that holds all the Mars' Data
    mars_info = {}
    # Execute Chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    #Visit the page using the browser
    browser.visit(url)
    # assign html content
    html = browser.html
    # Create a Beautiful Soup object
    soup = bs(html, "html.parser")
    # Extract the title
    news_title = soup.find_all('div', class_='content_title')[0].find('a').text.strip()
    # Extract the paragraph
    news_p = soup.find_all('div', class_='rollover_description_inner')[0].text.strip()
    # put infos into Library
    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p
    # Mars Space Images
    # URL of page
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    #Visit the page using the browser
    browser.visit(url_image)
    # assign html content
    html2 = browser.html
    # Create a Beautiful Soup object
    soup = bs(html2, "html.parser")
    #Scrape Path for the Feature Image. got the partial path of the url
    partial_address = soup.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()
    #combine the root url to get the full address
    featured_image_url = "https://www.jpl.nasa.gov"+partial_address
    # Put infos into Library
    mars_info['featured_image_url'] = featured_image_url

    # Mars Weather
    # Use splinter to scrape the latest Mars weather tweet
    url_twit= 'https://twitter.com/marswxreport?lang=en'
    #Visit the page using the browser
    browser.visit(url_twit)
    # assign html content
    html_twit = browser.html
    # Create a Beautiful Soup object
    soup_twit = bs(html_twit, "html.parser")
    #scrap latest Mars weather tweet
    mars_weather = soup_twit.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text
    # Put infos into Library
    mars_info['mars_weather'] = mars_weather
   
    # Mars Facts
    # Use Pandas to scrape the table

    url_facts = 'https://space-facts.com/mars/'
    # use Pandas to get the url table
    df = pd.read_html(url_facts)
    # Convert list of table into pandas dataframe
    df_mars = df[0]
    # update column name
    df_mars.columns=['description','value']
    #Set the index to the description column
    df_mars.set_index('description', inplace=True)
    # Use pandas to  generate HTML tables from DataFrames and save as html file
    mars_facts=df_mars.to_html(justify='left')
    # Put infos into Library
    mars_info['mars_facts'] = mars_facts

    # Mars Hemisperes
    # USGS Astrogeology site to obtain high resolution images
    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #Visit the page using the browser
    browser.visit(url_hemi)
    # assign html content
    html_hemi = browser.html
    # Create a Beautiful Soup object
    soup_hemi = bs(html_hemi,"html.parser")
    # assigned list to store:
    hemisphere_image_urls = []
    # create empty dict
    dict = {}
    # get all the title
    results = soup_hemi.find_all('h3')
    # Loop through each result
    for result in results:
        item = result.text
        time.sleep(1)    
        browser.click_link_by_partial_text(item)
        time.sleep(1)
        # assign html content
        html_m = browser.html
        # Create a Beautiful Soup object
        soup_m = bs(html_m,"html.parser")
        time.sleep(1)
        # Grab the image link
        link_m = soup_m.find_all('div', class_="downloads")[0].find_all('a')[0].get("href")
        time.sleep(1)
        # Pass title to Dict
        dict["title"]=item
        
        # Pass url to Dictionary
        dict["img_url"]=link_m
        # Append Dict to the list 
        hemisphere_image_urls.append(dict)
        
        dict = {}
        browser.click_link_by_partial_text('Back')
        time.sleep(1)
    
    mars_info['hemisphere_image_urls']=hemisphere_image_urls
    
    # Return Library
    return mars_info