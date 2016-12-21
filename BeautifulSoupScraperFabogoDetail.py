__author__ = 'gaurav'

import urllib2
from bs4 import BeautifulSoup
import csv

#
# url = 'http://www.fabogo.com/mumbai/salons-and-spas?sort=popularity&page='
def parse_salon(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    name = soup.find('h1').find('a')
    if name:
        name = name.get('title').encode('ascii', 'ignore')
    area = soup.find('div', class_='pt3')
    if area:
        area = area.get_text()
    telephone = soup.find('span', class_='fs110 lato fw900')
    if telephone:
        telephone = telephone.get_text()
    address = soup.find('p', class_='p10')
    if address:
        address = address.get('span')
    menu_image_links = ""
    timing = ""
    feature = ""
    if soup.find_all('a', class_=' ba border-radius-5 mr5 image'):
        for image_link in soup.find_all('a', class_=' ba border-radius-5 mr5 image'):
            menu_image_links += image_link.get('href') + '| '

    table = soup.find('table', class_='table text-center mr10')
    if table:
        for tr in table.find_all('tr'):
            timing += tr.get_text() + "| "
    list = soup.find_all('li', class_='mr15 pr15')
    if list:
        for li in list:
            feature += li.find('span').get_text() + '| '

    return [name, area, telephone, address, menu_image_links, timing, feature]
# item-name mb5 pb5 fs220 mt0 fw300 bbw no-border-mobile

