from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html.read(), 'html.parser')
#
# for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

pages = set()
random.seed(datetime.datetime.now())


# 获取页面中所有内连的列表
def get_internal_links(bs, include_url):
    include_url = '{}://{}'.format(urlparse(include_url).scheme, urlparse(include_url).netloc)
    internal_links = []
    for link in bs.find('a', href=re.compile('^(/|.*' + include_url + ')')):
        print(link)
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                print('internal_link: {}'.format(link.attrs['href']))
                if link.attrs['href'].startswith('/'):
                    internal_links.append(include_url + link.attrs['href'])
                else:
                    internal_links.append(link.attrs['href'])
    return internal_links


# 获取页面中所有外链的列表
def get_external_links(bs, exclude_url):
    external_links = []
    for link in bs.find_all('a', href=re.compile(r'^(http|www)((?!' + exclude_url + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                print('external_link: {}'.format(link.attrs['href']))
                external_links.append(link.attrs['href'])

    return external_links


def get_random_external_links(starting_page):
    print('starting_page: {}'.format(starting_page))
    html = urlopen(starting_page)
    bs = BeautifulSoup(html.read(), 'html.parser')
    external_links = get_external_links(bs, urlparse(starting_page).netloc)
    if len(external_links) == 0:
        print('No external links, looking around the site for one.')
        domain = '{}://{}'.format(urlparse(starting_page).scheme, urlparse(starting_page).netloc)
        internal_links = get_internal_links(bs, domain)
        return get_random_external_links(internal_links[random.randint(0, len(internal_links) - 1)])
    else:
        return external_links[random.randint(0, len(external_links) - 1)]


def follow_external_only(starting_site):
    external_link = get_random_external_links(starting_site)
    print('Random external link is: {}'.format(external_link))
    follow_external_only(external_link)


# try:
#     follow_external_only('http://oreilly.com')
# except TimeoutError as e:
#     print(e)
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print(e)

all_ext_links = set()
all_int_links = set()


def get_all_external_links(site_url):
    html = urlopen(site_url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    domain = '{}://{}'.format(urlparse(site_url).scheme, urlparse(site_url).netloc)
    print('site_url: '+site_url)
    print('domain: '+domain)
    internal_links = get_internal_links(bs, domain)
    external_links = get_external_links(bs, domain)
    for internal_link in internal_links:
        print(internal_link)
        if internal_link not in internal_links:
            internal_links.append(internal_link)
    for external_link in external_links:
        print(external_link)
        if external_link not in external_links:
            external_links.append(external_link)


get_all_external_links('http://oreilly.com')
