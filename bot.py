from typing import Text
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def top_trending_news():
    URL = "https://www.firstpost.com/category/world"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all(class_ = "main-title")
    link_text = ""
    for i in data:        
        result = i.get_text()
        print(result)
        
top_trending_news()
