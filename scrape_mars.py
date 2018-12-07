# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def scrape():
    #url of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    #Retrieve page
    response = requests.get(url)
    #Create BeautifulSoup object and parse the html page
    soup = BeautifulSoup(response.text, 'html.parser')

        # NASA Mars News titles
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title = soup.find('div', class_='content_title').text.strip()
    
    # NASA Mars News text
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_p = soup.find_all('div', class_='rollover_description_inner').text.strip()
    
    # JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image = soup.find('img', class_='thumb').get('src')
    featured_image_url = 'https://www.jpl.nasa.gov' + image
    
    # Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets = soup.find('li', class_='js-stream-item')
    weather = ''
    for tweet in tweets:
        if 'Sol' not in weather:
            weather = tweets.find('div', class_='js-tweet-text-container')
            mars_weather = weather.p.text
    
    # Mars Facts        
    mars_df = pd.read_html('http://space-facts.com/mars/',attrs={'id':'tablepress-mars'})
    mars_df[0]
    
    # Mars Hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    title=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles_list = soup.find_all('div', class_='description')
    for titles in titles_list:
        t = titles.h3.text
        title.append(t)

    urls_list=['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 
                'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
                'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
                'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
    image_url=[]
    for urls in urls_list:
        url = urls
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image = soup.find('a', attrs={'target':'_blank', 'href': re.compile('^http://')})
        image_link = image.get('href')
        image_url.append(image_link)
    
    hemisphere_image_urls=[]
    for i in range(len(title)):
        d = dict([('title', title[i]), ('img_url', image_url[i])])
        hemisphere_image_urls.append(d)
    
    # # Create combine dict
    mars_data = {
        'latest_title': news_title,
        'latest_paragraph': news_p,
        'image_url': featured_image_url,
        'weather': mars_weather,
        'data_table': mars_df[0],
        'hemispheres': hemisphere_image_urls
    }
    
    return mars_data