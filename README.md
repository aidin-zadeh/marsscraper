# Mars Scarper

This repository contains a Python project that illustrates a web application scraping various websites for data related to the Mission to Mars. The current implementation of this project implements the following objectives:
- Perform scraping by [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) a python library for pulling data from html and xml files.
- Store/Retrieve data from MangoDB by [pymongo](https://api.mongodb.com/python/current/)
- Display scraped data by a web APP implemented with [Flask](http://flask.pocoo.org/) a micro web development framework based on Werkzeug

## Methodology

## Data
The data utilized in this project were scraped from the following sources:
- [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
- [JPL Mars Space Images](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
- [Mars Weather Twitter Account](https://twitter.com/marswxreport?lang=en)
- [Mars Fact Web Page](https://space-facts.com/mars/)
- [USGS Asterogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

## Report

## Requirements
- python            3.6.6
- numpy             1.14.5
- jupyter           1.0.0
- notebook          5.6.0
- pandas            0.23.3
- beautifulsoup4    4.6.0
- splinter          0.8.0
- selenium          3.13.0
- flask:            1.0.2
- pymongo           3.7.0 

## Directory Structure
```
.
├── docs                <- Documents related to this project.
├── images              <- Images for README.md files.
├── marsscraper         <- source files used in this project.
│   ├── conf
│   ├── data
│   │   ├── ext
│   │   ├── int
│   │   └── raw
│   └── scripts
│       └── templates
├── notebooks           <- Ipythoon Notebook files
└── reports             <- Generated analysis as HTML, PDF, Latex, etc.
    ├── figures         <- Generated graphics and figures used in reporting.
    └── logs            <- Generated log files.         
```
## Installation
Install python dependencies from  `requirements.txt` using conda.
```bash
conda install --yes --file requirements.txt
```

Or create a new conda environment `<new-env-name>` by importing a copy of a working conda environment at the project root directory :`marsscraper.yml`.
```bash
conda env create --name <new-env-name> -f marsscraper.yml
```
## Usage
```bash
python -m marsscraper.scripts.webapp -h
usage: webapp.py [-h] [-s HOST] [-p PORT] [-w WEBDRIVER] [-d DRIVERPATH]

Runs Flask scrapper application server

optional arguments:
  -h, --help            show this help message and exit
  -s HOST, --host HOST  Host name to listen. Default=`127.0.0.1` (local host)
  -p PORT, --port PORT  Port to listen. Default=5000
  -w WEBDRIVER, --webdriver WEBDRIVER
                        Web driver name. Default=`chrome`
  -d DRIVERPATH, --driverpath DRIVERPATH
                        Web driver path. Default=`/usr/local/bin/chromedriver`

Example of use: `python -m marsscraper.scripts.webapp --host 127.0.0.1
--port 5000 --webdriver chrome --driverpath /usr/local/bin/chromedriver`

```
## References

## To Do
- [ ] TBA

## License 
MIT license

