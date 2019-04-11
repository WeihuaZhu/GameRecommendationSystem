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
from bs4 import BeautifulSoup
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def parse_google(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'pE8vnd GZjjfc'})
    # print result_block
    for result in result_block:
        jobtitle = result.find('div', attrs={'class': 'fheAoc nsol9b RgAZAc'}).get_text()
        attr1 = result.find('div', attrs={'class': 'wozmme'}).find_all('div', attrs={'class': 'k8RiQ nsol9b'})
        attr2 = result.find('div', attrs={'class': 'edeiNb'}).find_all('div', attrs={'class': 'Ug1maf BbiuWb'})
        source = result.find('span', attrs={'class': 'CjlJVc'}).find('a', attrs={'class': 'nsol9b'}).get_text()
        joburl = result.find('span', attrs={'class': 'CjlJVc'}).find('a', attrs={'class': 'nsol9b'}).get('href')
        joburl = urllib.parse.unquote(joburl)

        
        if len(attr1) == 2 and len(attr2) == 2:
            opconame = attr1[0].get_text()
            location = attr1[1].get_text()
            date = attr2[0].get_text()
            jobtype = attr2[1].get_text()
            description = result.find('span', attrs={'class': 'Cyt8W'})
            description = urllib.parse.unquote(description.get_text())

            print(date, jobtype, jobtitle)
            print(opconame, location)
            print(source)
            print(joburl)
            print(description)
            print('-----------')

            if description:
                data = {'keyword': keyword, 'opconame': opconame, 'location': location, 'source': source, 'joburl': joburl, 'date': date,'jobtitle': jobtitle, 'jobtype': jobtype, 'description': description}
                # data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
                found_results.append(data)

    return found_results
 
def scrape_google(keyword):
    try:
        assert isinstance(keyword, str), 'Search term must be a string'
        escaped_search_term = keyword.replace(' ', '+')
 
        google_url = 'https://www.google.com/search?q={}&ibp=htl;jobs#fpstate=tldetail&htidocid=DGll76udo4NGbIkhAAAAAA%3D%3D&htivrt=jobs'.format(keyword)
        response = requests.get(google_url, headers=USER_AGENT)
        response.raise_for_status()
        html = response.text

        str(html).encode('utf-8')

        found_results = parse_google(html, keyword)

        # f = open(keyword + '_source.txt', 'w')
        # soup = BeautifulSoup(html, 'html.parser')
        # print(soup.prettify(), file = f)
        # f.close()

        return found_results

    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")




if __name__ == '__main__':
    data = []
    roots = []
    try:
        results = scrape_linkedin(roots[0])
        data.append(results)
    except Exception as e:
        print(e)
    finally:
        sleep(random.uniform(0.5, 2.5))

    f = open('testresult.txt', 'w')
    print(data, file = f)
    f.close()


    for root in roots:
        try:
            results = scrape_linkedin(root)
            data.append(results)
        except Exception as e:
            print(e)
        finally:
            sleep(random.uniform(0.5, 2.5))

        f = open('result_' + str(root) + '_.txt', 'w')
        print(data, file = f)
        f.close()

    # print(html)
