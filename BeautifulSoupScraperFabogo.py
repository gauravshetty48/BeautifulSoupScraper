__author__ = 'gaurav'

import urllib2
from bs4 import BeautifulSoup
import csv
import BeautifulSoupScraperFabogoDetail


url = 'http://www.fabogo.com/mumbai/salons-and-spas?sort=popularity&page='
# def parse_salon(url):
#     page = urllib2.urlopen(url)
#     soup = BeautifulSoup(page)
#
#     name = soup.find('span', class_=' fs200 fw500 ')
#     area = soup.find('div', class_='pt3')

for r in range(1, 256):
    url_page = url + str(r)
    page = urllib2.urlopen(url_page)
    soup = BeautifulSoup(page)

    for div in soup.find_all('div', class_='relative border-radius-3 ba bg-white clearfix'):
        link = div.find('a', class_='border-left-radius-3 link-single-venue ').get('href')
        hero_image = div.find('img', class_='border-left-radius-3 fw300').get('src')
        data_row = [link, hero_image]
        data_remaining = BeautifulSoupScraperFabogoDetail.parse_salon(link)
        data_row += data_remaining
        print(data_row)
        data = []
        data.append(data_row)
        with open('links.csv', 'a+') as fp:
            if data_row in fp:
                pass
            else:
                a = csv.writer(fp, delimiter=',')
                a.writerow(data_row)