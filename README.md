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
