from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # Scraping NASA Mars News
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html_news = browser.html
    soup = bs(html_news,'html.parser')

    # News_title from
    news = soup.find_all('div',class_='content_title')
    titles =[]

    for n in news:
        titles.append(n)
    news_title = titles[1].text
    
    # News_ParagraphText
    news_p = soup.find('div',class_='article_teaser_body').text
    
    # JPL Mars Space Images - Featured Image
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    html_img = browser.html
    soupy = bs(html_img,'html.parser')
    latest_image = soupy.find_all('a', class_='fancybox')
    
    img_list=[]

    for i in latest_image:
        link=i['data-fancybox-href']
        img_list.append(link)

    final_url = f'https://www.jpl.nasa.gov{img_list[1]}'

    # Mars Weather @Twitter
    
    # Mars Facts
    facts=[]
    url_facts="https://space-facts.com/mars/"
    facts_df = pd.read_html(url_facts)

    for i in facts_df:
        facts.append(i)
    
    #Table scraped in html format
    facts_table=facts[0]
    facts_table.rename(columns={0:'',1:'Values'},inplace = True)
    facts_table = facts_table.set_index('')
    Mars_table = facts_table.to_html()

    #Mars Hemispheres
    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)

    html_hem = browser.html
    soup_hem = bs(html_hem,'html.parser')

    x=soup_hem.find_all('div',class_='description')

    name=[]
    urls=[]

    # Adding to the list for names of the Mars Hemispheres
    for i in x:
        name.append(i.h3.text)
    print(name)

    # Adding to the list for urls for the images of Mars Hemispheres
    for j in x:
        urls.append(j.a['href'])
    print(urls)

    # Getting the partial url for the extended image
    partial_url ='https://astrogeology.usgs.gov'

    # List to hold the image url to the full resolution image
    hem_image = []

    for u in range(len(urls)):
        extract = f'{partial_url}{urls[u]}'
        browser.visit(extract)
        html_hem_img = browser.html
        soup_hem_img = bs(html_hem_img,'html.parser')
        hem_image.append(soup_hem_img.find('li').a['href'])
 
    # Creatiing a dictionary for each hemisphere
    hemisphere_image_urls = [{'title':name[0],'img_url':hem_image[0]},
                         {'title':name[1],'img_url':hem_image[1]},
                         {'title':name[2],'img_url':hem_image[2]},
                         {'title':name[3],'img_url':hem_image[3]}]

    # Store the scraped data into a dictionary
    mars_data = {
        'news_title': news_title,
        'news_p': news_p,
        'final_url': final_url,
        'Mars_table' : Mars_table,
        'hemisphere_image_urls' : hemisphere_image_urls,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


