

# import dependencies
import time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from splinter import Browser


T = 1


def scrape(driver, driverpath):

    # set up spliter browser
    executable_path = {"executable_path": driverpath}

    ## Latest news
    # set up splinter browser
    with Browser(driver, **executable_path, headless=False) as browser:

        # visit url
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        time.sleep(T)
        # pull html text
        html = browser.html
        # parse html
        soup = BeautifulSoup(html, "html.parser")
        # grab news title
        news_title = soup.find("div", {"class": "bottom_gradient"}).text
        # grab news content
        news_content = soup.find("div", {"class": "rollover_description_inner"}).text

    # with Browser("chrome", **executable_path, headless=False) as browser:

        # Latest featured images
        # featured image url
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)
        time.sleep(T)
        # navigate to link
        browser.click_link_by_partial_text("FULL IMAGE")
        time.sleep(T)
        browser.click_link_by_partial_text("more info")
        time.sleep(T)
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
    # with Browser("chrome", **executable_path, headless=False) as browser:

        ## Latest weather
        url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url)
        # pull/off-load html text
        html = browser.html
        # parse html
        soup = BeautifulSoup(html, "html.parser")
        # grab latest tweet
        weather = soup.find("p",{"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}).text

    # with Browser("chrome", **executable_path, headless=False) as browser:

        ## Mars facts
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
    # with Browser("chrome", **executable_path, headless=False) as browser:

        ## Mars hemispheres
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        time.sleep(T)

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
            # get link to1 hemisphere page
            url_item = "https://astrogeology.usgs.gov" + item.a['href']

            #  pull/off-load heml text
            browser.visit(url_item)
            time.sleep(T)

            # off-load html text
            html_item = browser.html
            # parse html
            soup_item = BeautifulSoup(html_item, 'html.parser')
            image_url = soup_item.find('div', {"class": "downloads"}).find('li').a['href']

            hemisphere_image_urls.append(dict(title=title, url=image_url))
            # check on the retrieved link
            browser.visit(image_url)
            time.sleep(T)

    scarpe_dict =  dict(
        news_title=news_title,
        news_content=news_content,
        featured_image_url=featured_image_url,
        weather=weather,
        facts_html=facts_html,
        hemisphere_image_urls=hemisphere_image_urls,
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return scarpe_dict
