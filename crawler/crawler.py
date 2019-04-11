# web scraping script
# rewrite in Python 3
# Author: Andy Yao
# Version 1.4
# Date 04/11/2019
# 
# encoding=utf8

from time import sleep
import json
import re
import urllib
import requests
import random
import csv
from bs4 import BeautifulSoup
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def parse_review(html):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    rank = 1
    review = soup.find('div', attrs={'class': 'article-content'})
    # print(review.get_text())
    # verdict = soup.find('div', attrs={'class': 'review-bottom'}).get_text()
    paras = ["".join(x.findAll(text=True)) for x in review.findAllNext("p")]
    result = "\n\n".join(paras)
    # print(result)

    return result

def parse_url(html):
    soup = BeautifulSoup(html, 'html.parser')
 
    rank = 1
    div = soup.find('a', attrs={'class': 'jsx-2881975397'}).get('href')
    # url = div.find('a', attrs={'class': 'jsx-2881975397 review'}).get('href')
    # print(url)

    return div
 
def scrape_root(csvurl, index, title):
    try:
        assert isinstance(csvurl, str), 'Search term must be a url'
        escaped_search_term = csvurl.replace(' ', '+')
 
        # parse review url
        ign_url = 'https://www.ign.com'+ csvurl
        # print(ign_url)
        response = requests.get(ign_url, headers=USER_AGENT)
        response.raise_for_status()
        html = response.text
        str(html).encode('utf-8')

        review_url = parse_url(html)
        # print(review_url)

        # parse review content
        ign_url2 = 'https://www.ign.com'+ review_url
        # print(ign_url2)
        response2 = requests.get(ign_url2, headers=USER_AGENT)
        response2.raise_for_status()
        html2 = response2.text
        str(html2).encode('utf-8')

        review_text = parse_review(html2)
        # print(review_text)
        # f = open('source.txt', 'w')
        # soup = BeautifulSoup(html2, 'html.parser')
        # print(soup.prettify(), file = f)
        # f.close()
        data = {'game': title, 'index': index, 'gameurl': ign_url, 'review_url': review_url, 'review': review_text}
        # data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
        print(data)
        return data

    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")




if __name__ == '__main__':
    roots = []

    # read csv
    csvFile = open('ign.csv', 'r')
    reader = csv.reader(csvFile)
    for item in reader:
        # print(item)
        gameurl = item[3]
        if reader.line_num == 1 or item[4] == 'iPad' or item[4] == 'iPhone':
            continue
        if gameurl not in roots:
            data_url = {'title':item[2], 'url':item[3]}
            roots.append(data_url)
        if reader.line_num == 5:
            break


    # print(roots)

    data = []
    for i,root in enumerate(roots):
        print('Scraping game', root['title'])
        try:
            result = scrape_root(root['url'], i, root['title'])
            data.append(result)
        except Exception as e:
            print(e)
        finally:
            sleep(random.uniform(0.5, 2.5))

    f = open('result.txt', 'w')
    print(data, file = f)
    f.close()

