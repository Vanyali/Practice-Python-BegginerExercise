import requests
from bs4 import BeautifulSoup


base_url = 'http://www.nytimes.com'
r = requests.get(base_url, "html_parser")
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())