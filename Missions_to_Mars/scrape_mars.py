import os
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq
from urllib.parse import urlsplit
import requests
from splinter import Browser
from selenium import webdriver
import time

def init_browser():
    executable_path = {"executable_path": "/users/saba/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
    
def scrape():
    browser = init_browser()
    #visit mars
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    news = {}
    #scrape page into soup
    html = browser.html
    soup = bs(html, "hrml.parser")

    #Getting the title of news and paragraph:
    news["news_title"] = soup.find('div', class_="content_title").a.get_text()
    news["news_p"] = soup.find('div', class_="rollover_description_inner").get_text()


    #Getting images:
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    browser.click_link_by_partial_text('more info')
    time.sleep(1)

    html2 = browser.html
    soup = bs(html2, 'html.parser')
    ext= soup.find("article").find("figure", class_="lede").a["href"]
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + ext

    #storing this data into dictionary NEW
    new["featured_image_url"]


    #Checking Mars Wather and storing it
    url_twit = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_twit)
    html_twit = browser.html
    soup_twit = bs(html_twit, 'html.parser' )
    mars_weather = soup_twit.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()
    new["mars_weather"]

    #Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts 
    # about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.

    res = requests.get("https://space-facts.com/mars/")
    soup_fact = bs(res.text,'lxml')
    mars_profile = soup_fact.find("table", class_="tablepress tablepress-id-mars").text
    print(mars_profile)
    table = pd.read_html(res)
    print(table[0])

    #Converting tables to dataframe
    df_mars = table[0]
    df_mars.columns=["Description", "Value"]
    html_mars= df_mars.to_html()
    print(html_mars)

    #Visitng USGS to get high resolution images of Mars Hemisphere:
    url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemi)
    time.sleep(1)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(1)
    html_hemi = browser.html
    soup_hemi = BeautifulSoup(html_hemi, 'html.parser')

    cerb_link = soup_hemi.find("div", class_="downloads").a["href"]
    print(link)
    #getting all url's of images in a list:
    hemi_img_url = []
    # creating a dictionary:

    c = {
        "title": "Cerberus Hemisphere Enhanced",
        "img_url": cerb_link
    }
    # Append the dictionary to the list
    hemi_img_url.append(c)

    url2_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url2_hemi)
    time.sleep(1)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(1)
    html2_hemi = browser.html
    soup2_hemi = BeautifulSoup(html2_hemi, 'html.parser')

    schi_link = soup2_hemi.find("div", class_="downloads").a["href"]
    print(schi_link)

    schi_img_url = []
# creating a dictionary:

    schi = {
        "title": "Schiaparelli Hemisphere Enhanced",
        "img_url": schi_link
    }
    # Append the dictionary to the list
    schi_img_url.append(schi)
    
    url3_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url3_hemi)
    time.sleep(1)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(1)
    html3_hemi = browser.html
    soup3_hemi = BeautifulSoup(html3_hemi, 'html.parser')

    syr_link = soup3_hemi.find("div", class_="downloads").a["href"]
    print(syr_link)

    syr_img_url = []
# creating a dictionary:

    syr = {
        "title": "Syrtis Major Hemisphere Enhanced",
        "img_url": syr_link
    }
    # Append the dictionary to the list
    syr_img_url.append(syr)
    print(syr_img_url)

    url4_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url4_hemi)
    time.sleep(1)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(1)
    html4_hemi = browser.html
    soup4_hemi = BeautifulSoup(html4_hemi, 'html.parser')

    vall_link = soup4_hemi.find("div", class_="downloads").a["href"]
    print(vall_link)

    vall_img_url = []
# creating a dictionary:

    vall = {
        "title": "Valles Marineris Hemisphere Enhanced",
        "img_url": vall_link
    }
    # Append the dictionary to the list
    vall_img_url.append(vall)

    hemi_all=[]
    hemi_all.append(c)
    hemi_all.append(schi)
    hemi_all.append(syr)
    hemi_all.append(vall)
    print(hemi_all)