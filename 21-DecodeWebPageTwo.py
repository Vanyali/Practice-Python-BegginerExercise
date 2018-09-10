import requests
from bs4 import BeautifulSoup

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

def save_in_file(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    with open("RobotScraper.txt", "w") as textfile:
        for txt in soup.find_all('p'):
            textfile.write(txt.text)

save_in_file(base_url)




