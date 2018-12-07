{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "# Dependencies\n",
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "outputs": [],
      "execution_count": 75,
      "metadata": {
        "inputHidden": false,
        "outputHidden": false
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def scrape():\n",
        "    #url of page to be scraped\n",
        "    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
        "    #Retrieve page\n",
        "    response = requests.get(url)\n",
        "    #Create BeautifulSoup object and parse the html page\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "\n",
        "    # NASA Mars News titles\n",
        "    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "    news_title = soup.find(\"div\", class_='content_title').text.strip()\n",
        "\n",
        "    # NASA Mars News text\n",
        "    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "    news_p = soup.find_all(\"div\", class_='rollover_description_inner').text.strip()\n",
        "\n",
        "    # JPL Mars Space Images - Featured Image\n",
        "    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "    image = soup.find('img', class_=\"thumb\").get('src')\n",
        "    featured_image_url = 'https://www.jpl.nasa.gov' + image\n",
        "\n",
        "    # Mars Weather\n",
        "    url = 'https://twitter.com/marswxreport?lang=en'\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "    tweets = soup.find('li', class_='js-stream-item')\n",
        "    weather = ''\n",
        "    for tweet in tweets:\n",
        "        if 'Sol' not in weather:\n",
        "            weather = tweets.find('div', class_='js-tweet-text-container')\n",
        "            mars_weather = weather.p.text\n",
        "\n",
        "    # Mars Facts        \n",
        "    mars_df = pd.read_html('http://space-facts.com/mars/',attrs={'id':'tablepress-mars'})\n",
        "    mars_df[0]\n",
        "\n",
        "    # Mars Hemisphere\n",
        "\n",
        "    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
        "    title=[]\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.text, 'html.parser')\n",
        "    titles_list = soup.find_all('div', class_='description')\n",
        "    for titles in titles_list:\n",
        "        t = titles.h3.text\n",
        "        title.append(t)\n",
        "\n",
        "    urls_list=['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', \n",
        "               'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',\n",
        "               'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',\n",
        "               'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']\n",
        "    image_url=[]\n",
        "    for urls in urls_list:\n",
        "        url = urls\n",
        "        response = requests.get(url)\n",
        "        soup = BeautifulSoup(response.text, 'html.parser')\n",
        "        image = soup.find('a', attrs={'target':'_blank', 'href': re.compile(\"^http://\")})\n",
        "        image_link = image.get('href')\n",
        "        image_url.append(image_link)\n",
        "\n",
        "    hemisphere_image_urls=[]\n",
        "    for i in range(len(title)):\n",
        "        d = dict([(\"title\", title[i]), (\"img_url\", image_url[i])])\n",
        "        hemisphere_image_urls.append(d)\n",
        "\n",
        "     # # Create combine dict\n",
        "        mars_data = {\n",
        "            'latest_title': news_title,\n",
        "            'latest_paragraph': news_p,\n",
        "            'image_url': featured_image_url,\n",
        "            'weather': mars_weather,\n",
        "            'data_table': mars_df[0],\n",
        "            'hemispheres': hemisphere_image_urls\n",
        "        }\n",
        "\n",
        "    return mars_data\n",
        "        "
      ],
      "outputs": [],
      "execution_count": 33,
      "metadata": {
        "inputHidden": false,
        "outputHidden": false
      }
    }
  ],
  "metadata": {
    "kernel_info": {
      "name": "python3"
    },
    "kernelspec": {
      "name": "python3",
      "language": "python",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python",
      "version": "3.6.5",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "nteract": {
      "version": "0.12.3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}