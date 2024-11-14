from bs4 import BeautifulSoup as BS4
from selenium import webdriver

import time

BASE_URL = "https://robota.ua"
driver = webdriver.Firefox()

def request_to_site(url: str) -> str:
    """
        Makes a GET request to the specified URL and returns the HTML content of the page
    """
    driver.get(url)
    html_content = driver.page_source
    return html_content


def get_titles(html_content: str) -> list:
    soup = BS4(html_content, "html.parser")
    titles_list = soup.find_all("p", {"class": "santa-m-0 santa-typo-h3 santa-pb-10"})
    return titles_list


def get_links(html_content: str) -> list:
    soup = BS4(html_content, "html.parser")
    dives = soup.find_all("a", {"class": "santa-no-underline"})
    return [(BASE_URL + item.get("href")) for item in dives]
    
html_content = request_to_site("https://robota.ua/ru/candidates/python-developer/kyiv?rubrics=%5B%221%22%5D")
time.sleep(3)
print(get_links(html_content))
driver.quit()








