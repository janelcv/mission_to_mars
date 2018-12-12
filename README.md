# mission_to_mars

## Introduction

Congratulations! You just won a ticket to Mars! 
Your mission beggins today, but first, let's find out what how does this planet look like and what's happening there.

## Methodology
[mission_to_mars.ipynb]() Jupyter notebook was used for extracting data from various websites:
1. [NASA Science](https://mars.nasa.gov/news/)
2. [NASA Jet Propulsion Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
3. [Mars Weather Twitter](https://twitter.com/marswxreport?lang=en)
4. [Space Facts](http://space-facts.com/mars/)
5. [Astrogeology Science Center](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

Jupyter notebook [mission_to_mars.ipynb](https://github.com/janelcv/mission_to_mars/blob/master/mission_to_mars.ipynb) was converted into __scrape()__  function and stored as python file [scrape_mars.py]().

In addition, __Flask__  environment with two routes was created:
1.  `/scrape`  which imports  `scrape_mars.py` script and calls  `scrape` function.
2. `/` which query  Mongo database and pass the mars data into an HTML template to display the data.


### Extraction

Data was extracted using Python (version 3.6) [Pandas](https://pandas.pydata.org/pandas-docs/stable/) module  in [mission_to_mars.ipynb](https://github.com/janelcv/mission_to_mars/blob/master/mission_to_mars.ipynb)  Jupyter Notebook. 

```python
# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
browser = Browser('chrome')
import requests
import pandas as pd
import numpy as np
import re
import json
```
[BeautifulSoup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)) was used to scrape information from various websites

```python

#url of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

#Retrieve page
response = browser.visit(url)

#Create BeautifulSoup object and parse the html page
soup = BeautifulSoup(response.text, 'html.parser')
```
