import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def get_page(site):
    request = requests.get(site)
    return BeautifulSoup(request.text, 'html.parser')


def scrape_ny_times(site):
    bs = get_page(site)
    title = bs.find('h1').text
    lines = bs.find_all('p', {'class': 'story-content'})
    body = '\n'.join([line.text for line in lines])
    return Content(site, title, body)


def scrape_brookings(site):
    bs = get_page(site)
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'post-body'}).text
    return Content(site, title, body)


# scrape_site = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3' \
#               '-uncomfortable' \
#               '-truths/ '
# content = scrape_brookings(scrape_site)
# print('Title:{}'.format(content.title))
# print('URL:{}\n'.format(content.url))
# print(content.body)

scrape_url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
content = scrape_ny_times(scrape_url)
print('Title:{}'.format(content.title))
print('URL:{}\n'.format(content.url))
print(content.body)
