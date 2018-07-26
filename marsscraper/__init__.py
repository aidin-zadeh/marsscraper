

# import dependencies
import time
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser


def scrape():

    # set up spliter browser
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}

    ## Latest news
    # set up splinter browser
    with Browser("chrome", **executable_path, headless=True) as browser:

        # visit url
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)

        # pull html text
        html = browser.html

    # parse html
    soup = BeautifulSoup(html, "html.parser")

    #grab needed info
    news_title = soup.find('div', class_="bottom_gradient").text
    news_content = soup.find('div', class_="rollover_description_inner").text


    ## Latest featured images
    # set up splinter browser
    with Browser("chrome", **executable_path, headless=False) as browser:
        # featured image url
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)
        time.sleep(4)
        #navigate to link
        browser.click_link_by_partial_text("FULL IMAGE")
        time.sleep(2)

        browser.click_link_by_partial_text("more info")

        # pull/off-load html text
        html = browser.html

    # parse html
    soup = BeautifulSoup(html, "html.parser")

    # grab the image path
    image_path = soup.find('figure', class_='lede').a['href']
    # make the full path
    featured_image_url = "https://www.jpl.nasa.gov/" + image_path


    # # grab the image path
    # image_path = soup.find("div", {"class": "download_tiff"}).p.a["href"]
    # # make the full path
    # featured_image_url = "https://www.jpl.nasa.gov/" + image_path


    ## Latest weather
    # set up splinter browser
    with Browser("chrome", **executable_path, headless=False) as browser:
        url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url)

        # pull/off-load html text
        html = browser.html

    # parse html
    soup = BeautifulSoup(html, "html.parser")
    # grab latest tweet
    weather = soup.find("p",{"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}).text

    ## Mars facts
    # set up splinter browser
    with Browser("chrome", **executable_path, headless=False) as browser:
        url = "https://space-facts.com/mars/"
        browser.visit(url)

        # pull/off-load html text
        html = browser.html

    # parse html
    soup = BeautifulSoup(html, "html.parser")
    #get the entire table
    facts_table = soup.find('table',
                    {"class": "tablepress tablepress-id-mars"}
                   ).find_all("tr")

    facts_dict = dict(label=[], value=[])
    for tr in facts_table:
        elements = tr.find_all("td")
        facts_dict["label"].append(elements[0].text)
        facts_dict["value"].append(elements[1].text)

    facts_df = pd.DataFrame(facts_dict)
    facts_html = facts_df.to_html(header=False, index=False)


    ## Mars hemispheres
    # set up splinter browser
    with Browser("chrome", **executable_path, headless=False) as browser:
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        time.sleep(5)

        # pull/off-load html text
        html = browser.html
        # parse html
        soup = BeautifulSoup(html, "html.parser")

        # get class holding hemisphere picture
        collapsible_results = soup.find("div", {"class": "collapsible results"})
        hemispheres = collapsible_results.find_all("div", {"class": "description"})

        hemisphere_image_urls = []

        for item in hemispheres:
        # get title
        title = item.a.h3.text
        # get link to hemisphere page
        url_item = "https://astrogeology.usgs.gov" + item.a['href']

        #  pull/off-load heml text
        browser.visit(url_item)
        time.sleep(1)

        # off-load html text
        html_item = browser.html
        # parse html
        soup_item = BeautifulSoup(html_item, 'html.parser')
        image_url = soup_item.find('div', {"class": "downloads"}).find('li').a['href']

        hemisphere_image_urls.append(dict(title= title, image_url= image_url))
        # check on the retrieved link
        browser.visit(image_url)
        time.sleep(5)

    scarpe_dict =  dict(
        news_title=news_title,
        news_content=news_content,
        featured_image_url=featured_image_url,
        weather=weather,
        facts_html=facts_html,
        hemisphere_image_urls=hemisphere_image_urls,
    )
    return scarpe_dict
