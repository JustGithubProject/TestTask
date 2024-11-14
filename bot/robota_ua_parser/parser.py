from bs4 import BeautifulSoup as BS4
from selenium import webdriver

from robota_ua_parser.constants import BASE_URL


def request_to_site(url: str) -> str:
    """
        Makes a GET request to the specified URL and returns the HTML content of the page
    """
    driver = webdriver.Firefox()
    driver.get(url)
    html_content = driver.page_source
    return html_content, driver


def get_titles(html_content: str) -> list:
    """
        Extracts all resume titles from the HTML content.
    """
    soup = BS4(html_content, "html.parser")
    titles_list = soup.find_all("p", {"class": "santa-m-0 santa-typo-h3 santa-pb-10"})
    return titles_list


def get_links(html_content: str) -> list:
    """
        Extracts all links associated 
        with resume titles from the HTML content.
    """
    soup = BS4(html_content, "html.parser")
    dives = soup.find_all("a", {"class": "santa-no-underline"})
    return [(BASE_URL + item.get("href")) for item in dives if item.get("href").startswith("/ru/candidates/")]


def get_resumes(html_content: str) -> list:
    """
        Aggregates resume data including title, 
        owner information, and links into structured dictionary objects.
    """
    # titles = get_titles(html_content)
    links = get_links(html_content)
    return links







