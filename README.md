# NexaCrawler

NexaCrawler is a Python web scraping project built using Scrapy. It is designed to crawl the website "http://books.toscrape.com/" and extract information about various books available on the website, including their titles, prices, and availability.

## Requirements

- Python 3.x
- Scrapy

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python installed. If not, you can download it from the official website: https://www.python.org/downloads/
3. Install Scrapy by running the following command in your terminal or command prompt:

```bash
pip install scrapy
```
## Usage

To start crawling and extract book information, follow these steps:

Navigate to the project directory where the CrawlingSpider class is located.
Open the terminal or command prompt in that directory.
Run the following command:
```bash
scrapy crawl comecrawler
```
The crawler will start visiting pages on the "http://books.toscrape.com/" website, extract the book titles, prices, and availability, and save the results in the output format specified in the parse_item method.

## Configuration

name: The name of the spider is set to "comecrawler."
allow_domains: The spider is allowed to crawl pages only from "toscrape.com."
start_urls: The spider will start its crawling process from the URL "http://books.toscrape.com/".
PROXY_SERVER: The proxy server IP address used for crawling. (In this example, it is set to "50.63.165.137").
rules: The spider uses two rules for crawling:
The first rule allows crawling URLs with the pattern "catalogue/category."
The second rule allows crawling URLs with the pattern "catalogue" but denies URLs with the pattern "category". The parse_item method is used to extract book information from these URLs.

Before running the crawler, make sure you have permission to scrape the target website. Be respectful to website owners and comply with their terms of service.

## Happy crawling! 🕷️
