import requests
from bs4 import BeautifulSoup
import pprint
# vitual web browser with request.get
res = requests.get('https://news.ycombinator.com/news')

# BeautifulSoup to read the web content
soup = BeautifulSoup(res.text, 'html.parser')
soup.body.contents

# Find web elements with BeautifulSoup
soup.find_all('div') # find all
soup.find('div') # find first

soup.find(id='25029484') # find element with id
soup.select('.score') # find element with class

# BeautifulSoup with css selectors
soup.select('.score')
links = soup.select('.storylink')
links[0]

votes = soup.select('.score')
votes[0]
votes[0].get('id')
votes[0].get('class')

subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k: k['vote'])

def create_custome_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):

        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().split(' ')[0])
            if points > 99: 
                hn.append({'title': title, 'link': href, 'vote': points })
    return sort_stories_by_votes(hn)

pprint.pprint(create_custome_hn(links, subtext))

