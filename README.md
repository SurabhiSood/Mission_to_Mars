# Mission to Mars

A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.


## Step 1 - Scraping

Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* Scrape the (https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 

### JPL Mars Space Images - Featured Image

* url for JPL Featured Space Image @(https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* navigate the site using splinter to find the image url for the current Featured Mars Image.


### Mars Weather

* Scrape the latest Mars weather tweet from twitter.

### Mars Facts

* Using Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. from (https://space-facts.com/mars/)

### Mars Hemispheres

* high resolution images for each of Mar's hemispheres (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)



## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
