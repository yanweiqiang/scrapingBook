from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html5lib')

print(bs)

# nameList = bs.find_all('span', {'class': 'green'})
# nameList = bs.find_all(['h1', 'h2'])
# nameList = bs.find_all('span', {'class': {'green', 'red'}})
# nameList = bs.find_all(text='A Useful Page')
#
# for name in nameList:
#     print(name.get_text())

# for child in bs.find('table', {'id': 'giftList'}).children:
#     print(child)

# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)

# for sibling in bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_siblings:
#     print(sibling.get_text())


# images = bs.find_all('img', {'src': re.compile(r'\.\./img/gifts/img.*\.jpg')})
#
# for image in images:
#     print(image['src'])

bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
bs.find_all('', text='Or maybe he\'s only resting?')
