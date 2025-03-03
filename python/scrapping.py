import requests
from bs4 import BeautifulSoup
import schedule
import time

def fetchnews():
    apiUrl = "https://www.bbc.com/news"
    response = requests.get(apiUrl)
    print("Latest Headlines from across the world with BBC ... ")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all("h2")
        for d in data:
            print(f"Headline: {d.contents[0]}")

schedule.every(10).seconds.do(fetchnews)

while True:
    schedule.run_pending()
    time.sleep(1)
