import sys
import time
import requests
from bs4 import BeautifulSoup

def find_philosophy(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    if soup.find(id='firstHeading').text != 'Philosophy':
        print(soup.find(id='firstHeading').text)
        link = next((c.get('href') for p in soup.find(class_='mw-parser-output').findAll('p') for c in p.findAll('a') if c.get('href', '').startswith('/')), None)        
        
        if not link:
            print('Dead end :(', link) # Exit code 
            exit()

        url = 'http://en.wikipedia.org' + link
        time.sleep(0.5)
        find_philosophy(url)
    else:
        print("EUREKA! - You've reached Philosophy")



random_url = 'https://en.wikipedia.org/wiki/Special:Random'
user_input = input("Enter a Wikipedia URL: ")

if user_input:
    url = user_input
else:
    url = random_url
    print("No input found")
    print("Applying random URL")

find_philosophy(url)    