from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

myUrl = "http://www.pythonscraping.com/pages/page1.html"


def get_title(url):
    title = ""
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html5lib')
        title = bs.h1
        print(bs.h1)
        print(bs.find('nonExistingTag').find('anotherTag'))
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found!')
    except AttributeError as e:
        print('Tag was not found!')
    else:
        print('It worked!')
    return title


print(get_title(myUrl))
