import requests

from bs4 import BeautifulSoup as BS4

from work_ua_parser import constants
from work_ua_parser import filters


def request_to_site(url: str) -> str:
    """
        Makes a GET request to the specified URL and returns the HTML content of the page
        if the request is successful (status code 200).
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text


def get_titles(html_content) -> list:
    """
        Extracts all resume titles from the HTML content.
    """
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    h2_mt_0_content_all = [item.text for item in h2_mt_0_all]
    return h2_mt_0_content_all


def get_links(html_content: str) -> list:
    """
        Extracts all links associated 
        with resume titles from the HTML content.
    """
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    
    if not div_col_md_8:
        return []

    h2_mt_0_all = div_col_md_8.find_all("h2", {"class": "mt-0"})
    
    hrefs_content_all = []
    for item in h2_mt_0_all:
        a_tag = item.find("a")  
        if a_tag: 
            href = a_tag.get("href")
            if href:  
                hrefs_content_all.append(href)
                
    return hrefs_content_all


def get_owners_info(html_content: str) -> list:
    """
        Extracts owner information associated
        with each resume from the HTML content.
    """
    soup = BS4(html_content, "html.parser")
    div_col_md_8 = soup.find("div", {"class": "col-md-8"})
    p_mt_xs_mb_0 = div_col_md_8.find_all("p", {"class": "mt-xs mb-0"})
    p_mt_xs_mb_0_content_all = [item.text for item in p_mt_xs_mb_0]
    return p_mt_xs_mb_0_content_all


def get_resumes(html_content: str) -> list:
    """
        Aggregates resume data including title, 
        owner information, and links into structured dictionary objects.
    """
    titles = get_titles(html_content)
    owners_info = get_owners_info(html_content)
    links = get_links(html_content)
    
    cards = []
    min_length = min(len(titles), len(owners_info), len(links))
    print(f"Titles={len(titles)}; owners_info={len(owners_info)}; links={len(links)}")
    for i in range(min_length):
        card = {
            "title": titles[i],
            "owner_info": owners_info[i],
            "links": constants.BASE_URL + links[i]
        }
        cards.append(card)
    
    return cards
